#Aula1 do curso de python com Lira
#Aluno: Guglielmo Targino.
#Data:11jul24.
#Versão: v0

import pyautogui
import time
pyautogui.PAUSE=1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(10)
pyautogui.write("www.google.com/gmail")

pyautogui.press("enter")
time.sleep(10)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)
pyautogui.write("99GaA4ir")
pyautogui.press("enter")
time.sleep(15)
pyautogui.click(x=2507, y=126)
time.sleep(5)
pyautogui.press("enter")
time.sleep(5)
pyautogui.scroll(150)
time.sleep(5)
pyautogui.click(x=2238, y=625)
time.sleep(5)
pyautogui.press("enter")
