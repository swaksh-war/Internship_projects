import numpy as np
import cv2
import joblib
from face_detector import get_face_detector, find_faces

def calc_hist(img):
    """
    To calculate histogram of an RGB image

    Parameters
    ----------
    img : Array of uint8
        Image whose histogram is to be calculated

    Returns
    -------
    histogram : np.array
        The required histogram

    """
    histogram = [0] * 3
    for j in range(3):
        histr = cv2.calcHist([img], [j], None, [256], [0, 256])
        histr *= 255.0 / histr.max()
        histogram[j] = histr
    return np.array(histogram)




