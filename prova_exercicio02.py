'''
Utilize o programa de fila para preencher uma fila com números inteiros(isso está
pronto, meu exemplo em aula). Essa fila de números servirá de input para dois deques:
Par e Impar. Qdo o número deletado da fila for Par esse número deverá ser inserido no
deque PAR, qdo for ímpar deverá ser inserido no deque ÍMPAR
'''
import numpy as np
class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

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
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

    def passa_deque(self, valor, deque_impar, deque_par):
        if valor % 2 == 0:
            deque_par.insere_inicio(valor)
        else:
            deque_impar.insere_inicio(valor)

class Deque:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Início estiver na primeira posição
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Final estiver na última posição
        elif self.final == self.capacidade - 1:
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor



    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return

        # Possui somente um elemento
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        else:
            # Volta para a posição inicial
            if self.inicio == self.capacidade - 1:
                self.inicio = 0
            else:
                # Incrementar início para remover o início atual
                self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.inicio == 0:
            self.final = self.capacidade - 1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return

        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            print('O deque já está vazio')
            return

        return self.valores[self.final]

    def printa_deque(self):
        if self.__deque_vazio():
            print('Deque vazio')
        else:
            aux = self.inicio
            while(aux > self.final and aux <= self.capacidade - 1):
                print(self.valores[aux], end=" ")
                aux += 1
            aux = 0
            while(aux <= self.final):
                print(self.valores[aux], end=" ")
                aux += 1

fila = FilaCircular(5)
fila.enfileirar(10)
fila.enfileirar(26)
fila.enfileirar(32)
fila.enfileirar(4)
fila.enfileirar(2)
deque_impar = Deque(5)
deque_par = Deque(5)
while(fila.numero_elementos > 0):
    aux = fila.desenfileirar()
    if(aux % 2 == 0):
        deque_par.insere_inicio(aux)
    else:
        deque_impar.insere_inicio(aux)
print("Deque impar: ")
deque_impar.printa_deque()
print('')
print("Deque par: ")
deque_par.printa_deque()
