from trainers_adnet_train_sl import adnet_train_sl
import argparse
from options_general import opts
from models_ADNet import adnet
from get_train_videos import get_train_videos
from trainers_adnet_train_rl import adnet_train_rl
import torch
import torch.backends.cudnn as cudnn
import torch.nn as nn
import os

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

parser = argparse.ArgumentParser(
    description='ADNet training')
parser.add_argument('--resume', default=None, type=str, help='Resume from checkpoint')
parser.add_argument('--num_workers', default=0, type=int, help='Number of workers used in dataloading')
parser.add_argument('--start_iter', default=0, type=int, help='Begin counting iterations starting from this value (should be used with resume)')
parser.add_argument('--cuda', default=True, type=str2bool, help='Use cuda to train model')
parser.add_argument('--gamma', default=0.1, type=float, help='Gamma update for SGD')
parser.add_argument('--visualize', default=False, type=str2bool, help='Use tensorboardx to for loss visualization')
parser.add_argument('--send_images_to_visualization', type=str2bool, default=False, help='Sample a random image from each 10th batch, send it to visdom after augmentations step')
parser.add_argument('--save_folder', default='weights', help='Location to save checkpoint models')

parser.add_argument('--save_file', default='ADNet_SL_', type=str, help='save file part of file name for SL')
parser.add_argument('--save_file_RL', default='ADNet_RL_', type=str, help='save file part of file name for RL')
parser.add_argument('--start_epoch', default=0, type=int, help='Begin counting epochs starting from this value')

parser.add_argument('--run_supervised', default=True, type=str2bool, help='Whether to run supervised learning or not')

parser.add_argument('--multidomain', default=True, type=str2bool, help='Separating weight for each videos (default) or not')

parser.add_argument('--save_result_images', default=True, type=str2bool, help='Whether to save the results or not. Save folder: images/')
parser.add_argument('--display_images', default=True, type=str2bool, help='Whether to display images or not')

args = parser.parse_args()

# Supervised Learning part
if args.run_supervised:
    opts['minibatch_size'] = 128
    # train with supervised learning
    _, _, train_videos = adnet_train_sl(args, opts)
    args.resume = os.path.join(args.save_folder, args.save_file) + '.pth'

    # reinitialize the network with network from SL
    net, domain_specific_nets = adnet(opts, trained_file=args.resume, random_initialize_domain_specific=True,
                                      multidomain=args.multidomain)

    args.start_epoch = 0
    args.start_iter = 0

else:
    assert args.resume is not None, \
        "Please put result of supervised learning or reinforcement learning with --resume (filename)"
    train_videos = get_train_videos(opts)
    opts['num_videos'] = len(train_videos['video_names'])

    if args.start_iter == 0:  # means the weight came from the SL
        net, domain_specific_nets = adnet(opts, trained_file=args.resume, random_initialize_domain_specific=True, multidomain=args.multidomain)
    else:  # resume the adnet
        net, domain_specific_nets = adnet(opts, trained_file=args.resume, random_initialize_domain_specific=False, multidomain=args.multidomain)

if args.cuda:
    net = nn.DataParallel(net)
    cudnn.benchmark = True

    net = net.cuda()

# Reinforcement Learning part
opts['minibatch_size'] = 32

net = adnet_train_rl(net, domain_specific_nets, train_videos, opts, args)



