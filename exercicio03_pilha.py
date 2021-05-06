'''
Escreva um algoritmo, usando uma Pilha, que inverte as letras de cada palavra de um texto terminado por ponto (.)
preservando a ordem das palavras. Por exemplo, dado o texto: ESTE EXERCÍCIO É MUITO FÁCIL. 
a.	A saída deve ser: ETSE OICÍCREXE É OTIUM LICÁF

'''
import numpy as np
class Pilha:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.topo = -1
    self.valores = np.chararray(self.capacidade, unicode=True)

  def pilha_cheia(self):
    if self.topo == self.capacidade - 1:
      return True
    else:
      return False

  def pilha_vazia(self):
    if self.topo == -1:
      return True
    else:
      return False

  def empilhar(self, valor):
    if self.pilha_cheia():
      print('A pilha está cheia')
    else:
      self.topo += 1
      self.valores[self.topo] = valor

  def desempilhar(self):
    if self.pilha_vazia():
      print('A pilha está vazia')
    else:
      self.topo -= 1

  def ver_topo(self):
    if self.topo != -1:
      return self.valores[self.topo]
    else:
      return -1

  def retorna_topo(self):
      if self.topo != -1:
          return self.topo
      else:
          return -1

  def printa_pilha(self):
        if self.topo == -1:
            print('Pilha vazia')
        else:
            for i in range(self.retorna_topo() + 1):
                print(self.valores[i], end=" ")
while(1):
    cont = 0
    frase = str(input('Digite uma expressão: '))
    for i in frase:
        if i == '.':
            cont = 1
    if cont == 1:
        break
    print('Frase sem . de final reescreva delimitando seu final')

pilha = Pilha(len(frase))
pilha_invertida = Pilha(len(frase))

for i in frase:
    if i == ' ' or i == '.':
        for j in range(pilha.retorna_topo() + 1):
            pilha_invertida.empilhar(pilha.ver_topo())
            pilha.desempilhar()
    pilha.empilhar(i)

pilha_invertida.printa_pilha()

