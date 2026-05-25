class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        preco_com_desconto = self.preco - (self.preco * (percentual / 100))
        return preco_com_desconto

produto_teste = Produto("Camiseta", 100.0)
novo_preco = produto_teste.desconto(10)

print(f"Produto: {produto_teste.nome}")
print(f"Preço original: R$ {produto_teste.preco:.2f}")
print(f"Preço com 10% de desconto: R$ {novo_preco:.2f}")