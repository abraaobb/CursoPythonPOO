from abc import ABC, abstractmethod


class MetodoPagamento(ABC):

    @abstractmethod
    def processar_pagamento(self, valor, moeda):
        pass


class PagamentoCartao(MetodoPagamento):
    def processar_pagamento(self, valor, moeda):
        print(f'A processar pagamento de {valor}{moeda} no cartão de crédito')


class PagamentoMBWay(MetodoPagamento):
    def processar_pagamento(self, valor, moeda):
        print(f'A processar pagamento de {valor}{moeda} via MBWay...')
