# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:08:36 2025

@author: Guglielmo H T

Exercício iniciando com biblioteca Numpy.
"""

import numpy as npy

print(npy.__version__)

arr1=npy.array([10,12,13])
print(arr1[1])

print(type(arr1))
arr1[1]=500

print(arr1[1])
