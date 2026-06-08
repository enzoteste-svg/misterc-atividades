class Pagamento:
    def processar(self, valor):
        return valor

class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95

class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02

class Pix(Pagamento):
    def processar(self, valor):
        return valor

metodos_pagamento = [Dinheiro(), Cartao(), Pix()]
valor_compra = 100.0

for metodo in metodos_pagamento:
    nome_metodo = metodo.__class__.__name__
    valor_final = metodo.processar(valor_compra)
    print(f"Forma: {nome_metodo} Valor Final: R$ {valor_final:.2f}")