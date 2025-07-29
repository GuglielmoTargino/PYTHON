# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 20:23:22 2025

@author: Guglielmo H T
"""

import pyautogui
import csv
import time

# Tempo para abrir o navegador e deixar na página
print("Você tem 5 segundos para deixar o navegador pronto...")
time.sleep(5)

with open('C:/Users/Guglielmo H T/Desktop/usuario.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.DictReader(csvfile)

    for linha in leitor:
        nome = linha['nome']
        email = linha['email']
        senha = linha['senha']

        # Clica e digita o nome
        pyautogui.click(676,402)
        pyautogui.write(nome)
        time.sleep(0.5)

        # Clica e digita o email
        
        #pyautogui.click(300, 300)
        #pyautogui.write(email)
        #time.sleep(0.5)

        # Clica e digita a senha
        
        #pyautogui.click(300, 350)
        #pyautogui.write(senha)
        #time.sleep(0.5)

        # Clica no botão enviar
        
        #pyautogui.click(400, 400)
        time.sleep(2)

        # Espera um pouco antes de ir pro próximo
        # (você pode adicionar navegação de volta aqui se necessário)
