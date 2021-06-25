import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
from scipy import ndimage

one = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat_images/BAGGAGE_20170522_113049_80428_A.jpg")
two = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat_images/BAGGAGE_20170522_115645_80428_B.jpg")
three = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat_images/BAGGAGE_20170523_085803_80428_D.jpg")
four = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat_images/BAGGAGE_20170523_094231_80428_B.jpg")
five = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat_images/BAGGAGE_20170524_075554_80428_B.jpg")

bg1 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/BAGGAGE_20180811_175323_83216_B_1.jpg")
bg2 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/BAGGAGE_20180811_175328_83216_A_1.jpg")
bg3 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/S0210209058_20180811232942_L-1_1.jpg")
bg4 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/S0300542812_20180822020845_L-10_1.jpg")
bg5 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/S0320365070_20180821160850_L-12_5.jpg")

images = [one, two, three, four, five]
bg = [bg1, bg2 , bg3, bg4, bg5]

def rotate(image): #45 degree rotation
    img = np.copy(image)
    img = ndimage.rotate(img, 45, cval=255)
    return img


def image_resize(image, width , inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]
    r = width / float(w)
    dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

constants = [(i.shape[1]) for i in bg]
constants[3] = constants[3] - 550
for i in range(5):
    img = image_resize(rotate(images[i]), constants[i])
    cv2.imwrite("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat/"+str(i)+".jpg", img)