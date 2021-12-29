
import numpy as np
# https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
def overlap_ratio(rect1, rect2):
    assert isinstance(rect1, (list, np.ndarray)) and isinstance(rect2, (list, np.ndarray))

    if len(np.array(rect1).shape) == 2 and len(np.array(rect2).shape) == 2:

        iou = []
        for _rect1, _rect2 in zip(rect1, rect2):
          
            boxA = [_rect1[0], _rect1[1], _rect1[0] + _rect1[2], _rect1[1] + _rect1[3]]
            boxB = [_rect2[0], _rect2[1], _rect2[0] + _rect2[2], _rect2[1] + _rect2[3]]

            # determine the (x, y)-coordinates of the intersection rectangle
            xA = max(boxA[0], boxB[0])
            yA = max(boxA[1], boxB[1])
            xB = min(boxA[2], boxB[2])
            yB = min(boxA[3], boxB[3])

            # compute the area of intersection rectangle
            interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

            # compute the area of both the prediction and ground-truth
            # rectangles
            boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
            boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

            # compute the intersection over union by taking the intersection
            # area and dividing it by the sum of prediction + ground-truth
            # areas - the interesection area
            _iou = interArea / float(boxAArea + boxBArea - interArea)

            if _iou < 0:
                _iou = 0

            iou.append(_iou)
    else:
        assert len(np.array(rect1).shape) == len(np.array(rect2).shape)

        boxA = [rect1[0], rect1[1], rect1[0] + rect1[2], rect1[1] + rect1[3]]
        boxB = [rect2[0], rect2[1], rect2[0] + rect2[2], rect2[1] + rect2[3]]

        # determine the (x, y)-coordinates of the intersection rectangle
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        # compute the area of intersection rectangle
        interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

        # compute the area of both the prediction and ground-truth
        # rectangles
        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        iou = interArea / float(boxAArea + boxBArea - interArea)

        if iou < 0:
            iou = 0

    # return the intersection over union value
    return iou
