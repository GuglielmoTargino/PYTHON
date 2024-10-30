#exercício com expressões regulares
# https://docs.python.org/3.9/library/re.html
#Aluno:GuglielmoTargino.
#Dta:30out24
#versão:v0.



import re

texto1='minha rota minha vidaaa! guglielmotargino@gmail.com'
texto2 = "Contatos: pessoa1@example.com, suporte@dominio.org, e teste.email@empresa.com.br"

ocorrencias = re.findall(r'a', texto1, re.IGNORECASE)
print(f"A letra 'a' aparece {len(ocorrencias)} vezes.")



emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto1)
print("E-mails encontrados:", emails)

palavras_com_exclamacao = re.findall(r'\b\w+!', texto1)
print("Palavras com exclamação:",palavras_com_exclamacao)



