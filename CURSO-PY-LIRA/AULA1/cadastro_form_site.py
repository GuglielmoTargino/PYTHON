# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 21:49:09 2025

@author: Guglielmo H T
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
opcoes = Options()
opcoes.add_argument(r"user-data-dir=C:/Users/Guglielmo H T/AppData/Local/Google/Chrome/User Data")
import csv
import time

# Configura o driver do Chrome
#driver = webdriver.Chrome(options=opcoes)
driver = webdriver.Chrome()

# Abre o site de cadastro
driver.get('localhost/tb_7sem_tela_farm')

# Lê o CSV e preenche os formulários
with open('C:/Users/Guglielmo H T/Desktop/usuario.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.DictReader(csvfile)

    for linha in leitor:
        nome = linha['nome']
        email = linha['email']
        senha = linha['senha']

        # Preenche os campos (ajuste os seletores conforme o site)
        driver.find_element(By.ID, 'senha').send_keys(nome)
        #driver.find_element(By.ID, 'campo_email').send_keys(email)
        #driver.find_element(By.ID, 'campo_senha').send_keys(senha)

        # Clica no botão de enviar
       # driver.find_element(By.ID, 'botao_cadastrar').click()

        time.sleep(2)  # espera o cadastro completar

        # Volta para a página de cadastro para o próximo
        driver.get('localhost/tb_7sem_tela_farm')

# Fecha o navegador
driver.quit()


