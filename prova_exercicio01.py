'''
Crie uma lista não ordenada de números inteiros que tenha um método chamado
deleta_os_pequenos. Esse método terá a funcionalidade de deletar todos os números
menores que o informado, Por exemplo: na lista: Lista= 30,1,23,4,6,45,160,2 se eu
escolher deletar o número 23 a lista ficaria: Lista = 30,23,45,160
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

    def deleta_os_pequenos(self, valor):
        aux = self.ultima_posicao
        while(aux != -1):
            if self.valores[aux] < valor:
                self.deletador_fulminante(self.valores[aux])
            aux -= 1


vetor = VetorNaoOrdenado(7)
vetor.insere(4)
vetor.insere(99)
vetor.insere(7)
vetor.insere(9)
vetor.insere(-80)
vetor.insere(-2)
vetor.insere(5)

vetor.deleta_os_pequenos(7)

vetor.imprime()