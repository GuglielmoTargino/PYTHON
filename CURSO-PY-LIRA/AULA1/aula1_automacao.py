#Aula1 do curso de python com Lira
#Aluno: Guglielmo Targino.
#Data:11jul24.
#Versão: v0

import pyautogui as at
import time as tmp
import pandas as pd

tabela=pd.read_csv("clientes.csv")
print("olá futuro!")


at.PAUSE=4

#linha é uma variável cria pelo programador

at.press("win")
at.write("chrome")
at.press("enter")
tmp.sleep(5)

for linha in tabela.index:
    #comando para transformar em texto o que voltar da tabela
    palavra=str(tabela.loc[linha,"mes"])
    at.write(palavra)
    tmp.sleep(1)
    at.write(" ")
    tmp.sleep(1)






#pyautogui.press("enter")
#time.sleep(10)
#pyautogui.press("tab")
#pyautogui.press("tab")
#pyautogui.press("tab")
#pyautogui.press("tab")
#pyautogui.press("enter")
#time.sleep(4)
#pyautogui.write("99GaA4ir")
#pyautogui.press("enter")

