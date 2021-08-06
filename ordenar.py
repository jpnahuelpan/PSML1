#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Juan Pablo Nahuelpán 
import os
def ordenar(*args, inputFileType):
    i = 1
    for dir in *args:
        for fileName in os.listdir(dir):
            print(fileName)
            dst = "{}.{}".format(i, inputFileType)
            if fileName != dst:
                src = dir +'/'+ fileName
                dst = dir +'/'+ dst          
                os.rename(src, dst)
            else:
                pass 
            i += 1
dir = ("directorios")

ordenar(dir, "png")