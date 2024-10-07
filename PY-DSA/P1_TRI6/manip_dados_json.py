# -*- coding: utf-8 -*-
"""
#Aula DSA tr6.Manipulação de dados json
#Aluno Guglielmo Targino.
#versão v0
#Data 04out24
"""
from urllib.request import urlopen
import json



response= urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados=json.loads(response)

print(dados[0]['title'])


    
    