import cv2

# class ProcessingVariables:
#     erode = 2
#     threshold = 37
#     adjustment = 11
#     iterations = 3
#     blur = 3

# class ProcessingVariables:
#     erode = 1
#     threshold = 15
#     adjustment = 3
#     iterations = 2
#     blur = 11

class ProcessingVariables:
    threshold_type = cv2.ADAPTIVE_THRESH_MEAN_C
    erode = 1
    threshold = 15
    adjustment = 3
    iterations = 2
    blur = 11
