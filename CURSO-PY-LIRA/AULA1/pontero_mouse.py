# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 21:21:35 2025

@author: Guglielmo H T
"""

import pyautogui
import time

while True:
    x, y = pyautogui.position()  # pega a posição atual do mouse
    print(f"Posição do mouse: x={x}, y={y}")
    time.sleep(1)  # espera 1 segundo antes de mostrar de novo
