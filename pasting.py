
import numpy as np
import cv2
import matplotlib.pyplot as plt

one = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat/1.jpg")
two = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat/2.jpg")
three = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat/3.jpg")
four = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat/4.jpg")
zero = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/threat/0.jpg")

b1 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/BAGGAGE_20180811_175323_83216_B_1.jpg")
b2 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/BAGGAGE_20180811_175328_83216_A_1.jpg")
b3 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/S0210209058_20180811232942_L-1_1.jpg")
b4 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/S0300542812_20180822020845_L-10_1.jpg")
b5 = cv2.imread("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/background_images/S0320365070_20180821160850_L-12_5.jpg")

bg = [b1, b2, b3, b4, b5]
images = [zero, one, two, three, four]

images[0] = cv2.copyMakeBorder(zero, 87, 0, 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
images[1] = images[1][50:bg[1].shape[0]+50, :, :]
images[2] = images[2][50:bg[2].shape[0]+50, :, :]
images[3] = cv2.copyMakeBorder(three, 349, 0, 550, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
images[4] = images[4][118:bg[4].shape[0]+118, :, :]
#print([imgs[i].shape for i in range(5)])

def masked(image):
    img = np.copy(image)
    lower = np.array([240, 240, 240])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    img[mask != 0] = [0, 0, 0]
    return (img, mask)

for i in range(5):
    image, mask = masked(images[i])
    bg[i][mask == 0] = [0, 0, 0]
    image = np.multiply(image, 0.8)
    pasted = bg[i]+image
    cv2.imwrite("/home/chitra/Downloads/BaggageAI_CV_Hiring_Assignment (1) (1)/BaggageAI_CV_Hiring_Assignment/pasted/"+"pasted"+str(i)+".png", pasted)