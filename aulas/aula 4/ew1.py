class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: O preço não pode ser negativo.")

produto1 = Produto("Celular", 1500.0)
print(f"Produto: {produto1.get_nome()} | Preço: R$ {produto1.get_preco()}")

produto1.set_preco(1350.0)  
produto1.set_preco(-100)    
print(f"Preço atual: R$ {produto1.get_preco()}")