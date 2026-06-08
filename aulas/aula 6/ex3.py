class Forma:
    def area(self):
        return 0

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

formas_geometricas = [Triangulo(6, 4), Quadrado(5), Triangulo(10, 5), Quadrado(3)]

for forma in formas_geometricas:
    print(f"Área da forma: {forma.area()}")