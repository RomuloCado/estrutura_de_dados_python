'''
Dada uma fila de caracteres formada por uma sequência alternada de letras e dígitos,
construa um método que retorne uma fila na qual as letras são mantidas na sequência
original e os dígitos são colocados na ordem inversa.
a. Exemplos: A 1 E 5 T 7 W 8 G → A E T W G 8 7 5 1 3
b. C 9 H 4 Q 6 → C H Q 6 4 9 3
Como mostram os exemplos, as letras devem ser mostradas primeiro, seguidas dos
dígitos. Sugestões:
- usar uma fila e uma pilha;
- supor um método ehDigito() retorna booleano que retorna verdadeiro caso um
caractere seja um dígito.
'''

import numpy as np
class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.chararray(self.capacidade, unicode=True)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

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

  def retorna_topo(self):
      if self.topo != -1:
          return self.topo
      else:
          return -1

  def desempilhar(self):
    if self.pilha_vazia():
      print('A pilha está vazia')
    else:
      self.topo -= 1
      return self.valores[self.topo + 1]

  def ver_topo(self):
    if self.topo != -1:
      return self.valores[self.topo]
    else:
      return -1

caracter = input('Digite os componentes da fila: ')
fila = FilaCircular(len(caracter))
pilha = Pilha(len(caracter))
for i in caracter:
    if not i.isdigit():
        fila.enfileirar(i)
    else:
        pilha.empilhar(i)

for j in range(pilha.retorna_topo()+1):
    fila.enfileirar(pilha.desempilhar())

print(fila.valores)
