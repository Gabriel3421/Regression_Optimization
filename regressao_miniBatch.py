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

def norm(x):
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

altura = norm(altura)
peso = norm(peso)

#valores "preditos" iniciais
for i in range(0, len(peso)):
        y1.append(m*peso[i]+b)

def calcula_m_b(inicio, fim):
    global y1, altura,peso,erro,m,b, erro_atual
    #preencher vetor de erro
    for i in range(inicio,fim):
       erro.append(y1[i] - altura[i])

    #atualizando os valores de b e m    

    erro_b = 0   
    #somatorio do erro  
    for i in range(0,20):
       erro_b = erro_b + erro[i]
    erro_atual += erro_b 

    b = b - a*(erro_b/20)

    #Somatorio do erro * xi
    soma_erro = 0
    for i in range(0,20):
        soma_erro = soma_erro + (erro[i] * peso[i])

    m = m - a*(soma_erro/20)
    
    y1 = []
    erro = []

x = 0

a0 = 0
a1 = 20

while (x < 500):
    # Separando os lotes e atualizando os valores no final de cada lote

    calcula_m_b(0,20)
    print(m,' * X + ',b,'\n')

    #valores atualizados
    for i in range(0, len(peso)):
        y1.append( m*peso[i]+b)

    calcula_m_b(20,40)
    print(m,' * X + ',b,'\n')

    #valores atualizados
    for i in range(0, len(peso)):
        y1.append( m*peso[i]+b)

    calcula_m_b(40,60)
    print(m,' * X + ',b,'\n')

    #valores atualizados
    for i in range(0, len(peso)):
        y1.append( m*peso[i]+b)

    calcula_m_b(60,80)
    print(m,' * X + ',b,'\n')

    #valores atualizados
    for i in range(0, len(peso)):
        y1.append( m*peso[i]+b)

    calcula_m_b(80,100)
    print(m,' * X + ',b,'\n')

    #valores atualizados
    for i in range(0, len(peso)):
        y1.append( m*peso[i]+b)

    x+=1  
    
plp.title('Erro medio: ' + str(abs(erro_atual)/(100*500)))
plp.plot(peso,y1, color = 'black')
plp.scatter(peso, altura, color='#2C86AA', marker=".")
plp.show()