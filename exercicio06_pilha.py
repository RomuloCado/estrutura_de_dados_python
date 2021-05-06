'''
Desenvolva um código para simular o jogo Ball Sort Puzzle.
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
            return False
        else:
            self.topo += 1
            self.valores[self.topo] = valor
            return True

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
                print(i, '-', self.valores[i])

    def fechado(self):
        if (self.valores[0] == self.valores[1] == self.valores[2] == self.valores[3]):
            return True
        else:
            return False

p1 = Pilha(4)
p1.empilhar('A')
p1.empilhar('B')
p1.empilhar('A')
p1.empilhar('C')

p2 = Pilha(4)
p2.empilhar('A')
p2.empilhar('A')
p2.empilhar('C')
p2.empilhar('B')

p3 = Pilha(4)
p3.empilhar('C')
p3.empilhar('C')
p3.empilhar('B')

p4 = Pilha(4)
p4.empilhar('B')

p5 = Pilha(4)


def passar_topo_pilha(pilha_origem, pilha_destino):
    if pilha_origem.ver_topo() != pilha_destino.ver_topo() and not pilha_destino.pilha_vazia():
        print('NÃO É POSSÍVE PASSAR PARA ESSA PILHA, SOMENTE SE FOR OS MESMOS VALORES DE TOPO, OU TOPO VAZIO')
    else:
        if pilha_destino.empilhar(pilha_origem.ver_topo()):
            topo_apagado = pilha_origem.retorna_topo()
            pilha_origem.valores[topo_apagado] = ' '
            pilha_origem.desempilhar()



def printa_jogo(p1, p2, p3, p4, p5):
    for i in range(3, -1, -1):
        print(p1.valores[i], ' | ', p2.valores[i], ' | ', p3.valores[i], ' | ', p4.valores[i], ' | ', p5.valores[i], ' | ')
    print('p1 |  p2 |  p3 |  p4 |  p5 |')

def verifica_qual_pilha(pilha):
    if pilha == 'p1':
        return p1
    elif pilha == 'p2':
        return p2
    elif pilha == 'p3':
        return p3
    elif pilha == 'p4':
        return p4
    elif pilha == 'p5':
        return p5


while(True):
    printa_jogo(p1, p2, p3, p4, p5)
    if p1.fechado() and p2.fechado() and p3.fechado() and p4.fechado() and p5.fechado():
        print('PARABÉNS LEVEL CONCLUÍDO')
        break
    else:
        while (True):
            pilha_origem = str(input('Qual a pilha de origem da sua jogada: ')).lower()
            if pilha_origem == 'p1' or pilha_origem == 'p2' or pilha_origem == 'p3' or pilha_origem == 'p4' or pilha_origem == 'p5':
                break
            print('Pilha inválida, digite novamente')
        while (True):
            pilha_destino = str(input('Qual a pilha de destino da sua jogada: ')).lower()
            if pilha_destino == 'p1' or pilha_destino == 'p2' or pilha_destino == 'p3' or pilha_destino == 'p4' or pilha_destino == 'p5':
                break
            print('Pilha inválida, digite novamente')

        passar_topo_pilha(verifica_qual_pilha(pilha_origem), verifica_qual_pilha(pilha_destino))
