import re
import numpy as np
import math
import matplotlib.pyplot as plp
from scipy import stats

altura = []
peso = []
resposta = []
erro = []
b = 0 
m = 0 
a = 0.01
y1 = []
erro_atual = 0

def normaliza(x):
    return stats.zscore(x)

dados = open("weight_height_edit.txt", "r")
for line in dados:
    # separando as colunas
    line = line.strip()  # quebra no \n
    line = re.sub('\s+', ',', line)  # trocando os espaços vazios por virgula
    y, xa,xb = line.split(",")  # quebra nas virgulas e retorna 3 valores
    peso.append(float(xa))
    altura.append(float(xb))
    resposta.append(float(y))
dados.close()

altura = normaliza(altura)
peso = normaliza(peso)

#valores "preditos" iniciais
for i in range(0, len(peso)):
        y1.append(m*peso[i]+b)

x = 0

while (x < 500):
    
    #preencher vetor de erro
    for i in range(0,len(y1)):
       erro.append(y1[i] - altura[i])

    #atualizando os valores de b e m    
    erro_b = 0 
    #somatorio do erro   
    for i in range(0,len(erro)):
       erro_b = erro_b + erro[i]
    
    erro_atual = erro_b
    b = b - a*(erro_b/len(erro))

    soma_erro = 0
    #Somatorio do erro * xi
    for i in range(0, len(erro)):
        soma_erro = soma_erro + (erro[i] * peso[i])

    m = m - a*(soma_erro/len(erro))

    print(m,' * X + ',b,'\n')
    y1 = []
    erro = []
    #valores atualizados
    for i in range(0, len(peso)):
        y1.append( m*peso[i]+b)
    
    x+=1 
    
plp.title('Erro medio: ' + str(abs(erro_atual)/100))
plp.plot(peso,y1, color = 'black')
plp.scatter(peso, altura, color='#2C86AA', marker=".")
plp.show()














