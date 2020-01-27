import re
import numpy as np
import math
import matplotlib.pyplot as plp
from scipy import stats

altura = []
peso = []
resposta = []

b = 0
m = 0 
a = 0.55
y1 = []
erro_atual = 0
def norm(x):
    #normalização via zscore
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

x = 0

while (x < 100):
    
    #preencher erro
    erro = (y1[x] - altura[x])
    erro_atual += erro
    #atualizando os valores de b e m    
    b = b - a*(erro)

    m = m - a*(erro*peso[x])

    print(m,' * X + ',b,'\n')
    y1 = []

    #valores atualizados
    for i in range(0, len(peso)):
        y1.append( m*peso[i]+b)
    
    x+=1 
    
plp.title('Erro medio: ' + str(abs(erro_atual)/100))
plp.plot(peso,y1, color = 'black')
plp.scatter(peso, altura, color='#2C86AA', marker=".")
plp.show()














