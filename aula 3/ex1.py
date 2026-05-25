class Produto:
    def __init__(self, nome, preco):
        self.nome = nome    
        self.preco = preco  

produto1 = Produto("Notebook", 3500.00)
produto2 = Produto("Mouse Gamer", 150.00)

print(f"Produto 1: {produto1.nome} - R$ {produto1.preco:.2f}")
print(f"Produto 2: {produto2.nome} - R$ {produto2.preco:.2f}")