#execício com linguagem python do curso data Science Academy

import pandas as pd


df=pd.read_csv("C:/Users/Guglielmo H T/Desktop/Data_list.csv")
exibe=df['Store'].value_counts()
print(exibe)


