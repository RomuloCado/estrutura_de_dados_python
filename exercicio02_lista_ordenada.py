'''
	Crie um novo método INSERE_UNICO para a lista ordenada, nesse método não será permitido números repetidos
	Crie um método IMPRIME_INVERSO, ou seja: do maior valor para o menor
	Crie um novo método INSERE para a lista ordenada de tal modo que a lista fique em ordem decrescente.
'''

import numpy as np
class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def imprime_inverso(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao, 0, -1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        # O objetivo desse For é achar a posição de inserção
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    #

    def insere_decrescente(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        # O objetivo desse For é achar a posição de inserção
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] < valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def insere_unico(self, valor):
        if self.contador_ocorrencias(valor) == 1:
            print('valor ja inserido na lista')
        else:
            self.insere(valor)

    def contador_ocorrencias(self, valor):
        cont = 0
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                cont += 1
            elif self.valores[i] > valor:
                break
        return cont

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1

    #
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            # Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se não achou
            elif limite_inferior > limite_superior:
                return -1
            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                # Limite superior
                else:
                    limite_superior = posicao_atual - 1

    #
    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1

vetor = VetorOrdenado(10)
print('------------------------------------------------')

vetor.insere_unico(3)
vetor.insere_unico(3)
vetor.insere_unico(8)
vetor.insere_unico(4)
vetor.insere_unico(4)
vetor.insere_unico(8)
vetor.insere_unico(15)


vetor.imprime_inverso()
