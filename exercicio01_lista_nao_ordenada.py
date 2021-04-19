'''
1.	Crie um novo método INSERE_UNICO, nesse método não será permitido números repetidos
2.	Crie o método DELETADOR_FULMINANTE, esse método elimina todas as ocorrências de um número dado       
3.	Crie o método DELETADOR_CALMINHO, esse método elimina  as ocorrências de um número dado (até aqui é igual ao método EXCLUIR), 
    mas se existirem mais ocorrências ele deixa apenas a primeira ocorrência 
    2,3,56,4,9,3,45 --> 2,3,56,4,9,45 
    2,3,56,4,9,45 --> 2,56,4,9,45
'''

import numpy as np

class VetorNaoOrdenado:
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

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def pesquisar_segunda_ocorrencia(self, valor):
        cont = 0
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                cont += 1
                if(cont == 2):
                    return i
        return -1

    def insere_unico(self, valor):
        if self.contador_ocorrencias(valor) == 1:
            print('valor ja inserido na lista')
        else:
            self.insere(valor)

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

    def contador_ocorrencias(self, valor):
        cont = 0
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                cont += 1
        return cont

    def deletador_fulminante(self, valor):
        if self.contador_ocorrencias(valor) == 1:
            self.excluir(valor)
        else:
            for i in range(self.contador_ocorrencias(valor) + 1):
                self.excluir(valor)

    def deletador_calminho(self, valor):
        if self.contador_ocorrencias(valor) == 1:
            self.excluir(valor)
        else:
            for i in range(self.contador_ocorrencias(valor) - 1):
                for j in range(self.pesquisar_segunda_ocorrencia(valor), self.ultima_posicao):
                    self.valores[j] = self.valores[j + 1]
                self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(7)
print('------------------------------------------------')
vetor.insere(5)
vetor.insere(5)
vetor.insere(7)
vetor.insere(9)
vetor.insere(1)
vetor.insere(5)

vetor.deletador_calminho(5)

vetor.imprime()
