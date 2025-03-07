# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 18:36:19 2025

@author: Guglielmo H T
"""

import pandas as pd
dados={'estado':['sp','rj','pb'],'ano':[2022,2023,2024],'tx_desmprego':[2,3,4]}
from pd import DataFrame

df=DataFrame(dados)
df.head()