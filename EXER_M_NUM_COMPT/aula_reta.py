# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:02:58 2025

@author: Guglielmo H T y=ax+b
"""

import numpy as np

x=np.array([1,2,13,14])
y=np.array([2.2,1.6,1.1,1.3])


a,b=np.polyfit(x,y,1)

print(f"Equação ajustada: y={a:.2f}x + {b:.2f}")


