# matlab source:
# https://github.com/hellbell/ADNet/blob/master/utils/get_benchmark_path.m

def get_benchmark_path(bench_name):
    assert bench_name in ['vot14','vot13']

    if bench_name == 'vot14':
        video_path = 'datasets/data/vot14'
    # elif bench_name == 'vot14':
    #     video_path = 'datasets/data/vot14'
    else:
        video_path = 'datasets/data/vot13'

    return video_path
