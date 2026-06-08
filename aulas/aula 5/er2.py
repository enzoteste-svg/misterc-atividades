class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.year = ano

    def informacoes(self):
        print(f"Marca: {self.marca} Ano: {self.year}")

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

carro1 = Carro("Toyota", 2022, 4)
moto1 = Moto("Honda", 2023, 7)

carro1.informacoes()
print(f"Portas: {carro1.portas}\n")

moto1.informacoes()
print(f"Cilindradas: {moto1.cilindradas}")