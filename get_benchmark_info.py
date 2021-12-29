# matlab code:
# https://github.com/hellbell/ADNet/blob/master/utils/get_benchmark_info.m

import os

def get_benchmark_info(bench_name=None):
    if bench_name is None:
        bench_name = 'vot13-otb'

    bench_path = os.path.join('/content/drive/Shareddrives/ADNet-pytorch/ADNet_pytorch/utils/videolist', bench_name + '.txt')
    bench_file = open(bench_path, 'r')
    video_names = bench_file.read().split('\n')
    bench_file.close()

    return video_names
