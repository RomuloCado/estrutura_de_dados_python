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
