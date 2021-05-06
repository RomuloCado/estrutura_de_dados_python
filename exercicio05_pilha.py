'''
Suponha que uma pilha possua 4 valores na seguinte ordem: 1, 2, 3 e 4. Qual seria a
sequência correta de operações de empilhamento(E) e desempilhamento (D) para se
obter os registros na ordem 2 4 3 1?

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

  def desemplilhar_outra_pilha(self, p2):
      p2.empilhar(self.ver_topo())
      self.desempilhar()

p1 = Pilha(5)
p2 = Pilha(5)
p1.empilhar(1)
p1.empilhar(2)
p1.desemplilhar_outra_pilha(p2)
p1.empilhar(3)
p1.empilhar(4)
p1.desemplilhar_outra_pilha(p2)
p1.desemplilhar_outra_pilha(p2)
p1.desemplilhar_outra_pilha(p2)
p1.printa_pilha()
print('==============================')
p2.printa_pilha()
