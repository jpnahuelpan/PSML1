#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Juan Pablo Nahuelpán 
import os
import cv2 as cv
# from google.colab.patches import cv2_imshow as imshow
import numpy as np



# Recorte de imagen
def recorte_imagen(dir:str, imagen:str):
    img = cv.imread(dir + imagen, cv.IMREAD_UNCHANGED)

    print(img.shape)
    w = img.shape[1]
    h = img.shape[0]
    if (w >= 256) or (h >= 256):
        cropped_image = img[((h // 2)- 128):((h // 2)+ 128), ((w // 2)- 128):((w // 2)+ 128)]
        cv.imwrite("imagenes/cropped/" + imagen, cropped_image)
    else: 
        os.remove(dir + imagen)


def blanco_negro(dir:str, imagen:str):
    if(os.path.isfile(dir + imagen)):  
        grey_img = cv.imread(dir + imagen,0) 
        grey_img = cv.cvtColor(grey_img,cv.COLOR_GRAY2BGR)

        cv.imwrite(  "imagenes/bw/" + imagen, grey_img)

if __name__ == "__main__":
    os.mkdir("imagenes")
    os.mkdir("imagenes/bw")
    os.mkdir("imagenes/cropped")
    for fileName in os.listdir("DIV2K_train_LR_difficult"):
        print(fileName)
        
        recorte_imagen("DIV2K_train_LR_difficult/", str(fileName))
        blanco_negro("imagenes/cropped/", str(fileName))