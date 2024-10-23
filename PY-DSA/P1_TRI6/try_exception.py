#execício com linguagem python do curso data Science Academy
#Treino com a função reduce



try:
    f=open('C:/Users/Guglielmo H T/Desktop/testePp.txt','w')
    f.write('Gravando no arquivo')
except IOError:
    print('Erro de calculo')
    
else:
    print('arquivo gravado ok')
    f.close()