import argparse
import glob
import os
import numpy as np
from precision_plot import iou_precision_plot, distance_precision_plot

parser = argparse.ArgumentParser(
    description='ADNet create plot')

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

parser.add_argument('--bboxes_folder', default='results_on_test_images_part2/ADNet_RL_-0.5', type=str, help='location where bboxes files are saved')
parser.add_argument('--save_plot_folder', default=None, type=str, help='save plots folder')
parser.add_argument('--show_plot', default=False, type=str2bool, help='show plot or not')

args = parser.parse_args()

bboxes_files = glob.glob(os.path.join('results_on_test_images_part2', '*-bboxes.npy'))
# bboxes_files = glob.glob(os.path.join('results_on_test_images_part2','Human3-bboxes.npy'))
bboxes_files.sort(key=str.lower)

all_bboxes = []
all_gt = []
all_dataset_name = []

for bboxes_file in bboxes_files:
    dataset_name = os.path.basename(bboxes_file)[:-11]
    gt_file = os.path.join('results_on_test_images_part2', dataset_name + '-ground_truth.npy')

    bboxes = np.load(bboxes_file)
    gt = np.load(gt_file)

    all_bboxes.append(bboxes)
    all_gt.append(gt)
    all_dataset_name.append(dataset_name)

for idx, bboxes in enumerate(all_bboxes):
    if args.save_plot_folder is not None:
        save_plot_file = os.path.join(args.save_plot_folder, all_dataset_name[idx])
    else:
        save_plot_file = None

    iou_precisions = iou_precision_plot(bboxes, all_gt[idx], all_dataset_name[idx], show=args.show_plot,
                                        save_plot=save_plot_file)

    distance_precisions = distance_precision_plot(bboxes, all_gt[idx], all_dataset_name[idx], show=args.show_plot,
                                                  save_plot=save_plot_file)

# all dataset plot precision
if args.save_plot_folder is not None:
    save_plot_file = os.path.join(args.save_plot_folder, 'ALL')
else:
    save_plot_file = None

all_bboxes_merge = []
for bboxes in all_bboxes:
    all_bboxes_merge.extend(bboxes)

all_gt_merge = []
for gt in all_gt:
    all_gt_merge.extend(gt)

all_bboxes_merge = np.array(all_bboxes_merge)
all_gt_merge = np.array(all_gt_merge)

iou_precisions = iou_precision_plot(all_bboxes_merge, all_gt_merge, 'ALL', show=args.show_plot,
                                        save_plot=save_plot_file)

distance_precisions = distance_precision_plot(all_bboxes_merge, all_gt_merge, 'ALL', show=args.show_plot,
                                              save_plot=save_plot_file)

print('distance_precision in 20px: ', distance_precisions[21])