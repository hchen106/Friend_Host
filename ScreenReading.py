#from PIL import Image, ImageGrab
#import pyscreenshot as ImageGrab
import cv2
import mss
import numpy as np

ms = mss.mss()
screen = {"top": 40, "left": 0,"width":1000,"height":900}
while True:
    #capture screen pixel
    readscreen_pil = ms.grab(screen)
    #convert pixel to matrix and show it on cv2 
    cv2.imshow('screen', np.array(readscreen_pil))
    #press q to quit
    if cv2.waitKey(25) & 0XFF == ord('q'):
        cv2.destroyAllWindows()
        break
