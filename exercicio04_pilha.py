'''
Desenvolva uma operação para transferir elementos de uma pilha P1 para uma pilha
P2 (cópia).
'''

import numpy as np
class Pilha:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.topo = -1
    self.valores = np.empty(self.capacidade, dtype=int)

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

  def copia_pilha(self, pilha):
      for i in range(pilha.retorna_topo() + 1):
          self.empilhar(pilha.valores[i])

  def printa_pilha(self):
      if self.topo == -1:
          print('Pilha vazia')
      else:
          for i in range(self.retorna_topo() + 1):
              print(i, '-' , self.valores[i])

p1 = Pilha(5)
p1.empilhar(4)
p1.empilhar(3)
p1.empilhar(3)
p1.empilhar(45)
p1.empilhar(1)
print('-------------------------------------------------')
print('Valores de P1: ')
p1.printa_pilha()
print('-------------------------------------------------')
print('Valores de P2: ')
p2 = Pilha(p1.capacidade)
p2.copia_pilha(p1)
p2.printa_pilha()
