#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Juan Pablo Nahuelpán 

import os
import cv2 as cv
import numpy as np

os.mkdir("imagenes/dataset")
for fileNameA in os.listdir("imagenes/bw"):
    pathImgInA = os.path.join("imagenes/bw", fileNameA)
    for fileNameB in os.listdir("imagenes/cropped"):  
        pathImgInB = os.path.join("imagenes/cropped", fileNameB)
        if(fileNameA == fileNameB):
            fileNameAB = fileNameA
            pathImgInAB = os.path.join("imagenes/dataset", fileNameAB)
            imgA = cv.imread(pathImgInA, cv.IMREAD_COLOR)
            imgB = cv.imread(pathImgInB, cv.IMREAD_COLOR)
            imgAB = np.concatenate([imgA, imgB], 1)
            cv.imwrite(pathImgInAB, imgAB)