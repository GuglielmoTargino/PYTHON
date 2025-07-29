# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 21:49:09 2025

@author: Guglielmo H T
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Configura o driver do Chrome
driver = webdriver.Chrome()

# Abre o site de cadastro
driver.get('https://exemplo.com/cadastro')

# Lê o CSV e preenche os formulários
with open('usuarios.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.DictReader(csvfile)

    for linha in leitor:
        nome = linha['nome']
        email = linha['email']
        senha = linha['senha']

        # Preenche os campos (ajuste os seletores conforme o site)
        driver.find_element(By.ID, 'campo_nome').send_keys(nome)
        driver.find_element(By.ID, 'campo_email').send_keys(email)
        driver.find_element(By.ID, 'campo_senha').send_keys(senha)

        # Clica no botão de enviar
        driver.find_element(By.ID, 'botao_cadastrar').click()

        time.sleep(2)  # espera o cadastro completar

        # Volta para a página de cadastro para o próximo
        driver.get('https://exemplo.com/cadastro')

# Fecha o navegador
driver.quit()


