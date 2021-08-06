#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Juan Pablo Nahuelpán 
import os
import shutil

os.mkdir("dataset")
os.mkdir("dataset/train")
os.mkdir("dataset/test")
os.mkdir("dataset/val")

i = 1
for fileName in os.listdir("imagenes/dataset"):
    print(i)
    if i < 200:
        shutil.copy2("imagenes/dataset/" + fileName, 'dataset/train')
    elif i >= 200 and i < 225:
        shutil.copy2("imagenes/dataset/" + fileName, 'dataset/test')
    elif i >= 225 and i < 250:
        shutil.copy2("imagenes/dataset/" + fileName, 'dataset/val')
    else:
        break
    i += 1