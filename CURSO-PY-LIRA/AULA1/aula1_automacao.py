#Aula1 do curso de python com Lira
#Aluno: Guglielmo Targino.
#Data:11jul24.
#Versão: v0

import pyautogui
import time
import pandas

tabela=pandas.read_csv("clientes.csv")
print("olá futuro!")


pyautogui.PAUSE=4

#linha é uma variável cria pelo programador





pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)

for linha in tabela.index:
    #comando para transformar em texto o que voltar da tabela
    palavra=str(tabela.loc[linha,"mes"])
    pyautogui.write(palavra)
    time.sleep(1)
    pyautogui.write(" ")
    time.sleep(1)






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

