from model import PagamentoCartao, PagamentoMBWay

if __name__ == '__main__':
    pagamento_cartao = PagamentoCartao()
    pagamento_mbway = PagamentoMBWay()

    pagamento_cartao.processar_pagamento(25, "R$")
    pagamento_mbway.processar_pagamento(73, "$")
