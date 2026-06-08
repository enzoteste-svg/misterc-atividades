class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0  

    def acelerar(self):
        self.velocidade += 10  

    def frear(self):
        self.velocidade -= 10  
        if self.velocidade < 0:
            self.velocidade = 0  

meu_carro = Carro("Chevrolet", "Onix")

meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.acelerar()

meu_carro.frear()

print(f"Carro: {meu_carro.marca} {meu_carro.modelo}")
print(f"Velocidade final: {meu_carro.velocidade} km/h")