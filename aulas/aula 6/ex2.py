class Instrumento:
    def tocar(self):
        pass

class Violao(Instrumento):
    def tocar(self):
        print("Violão: Strum strum... Notas acústicas e suaves.")

class Bateria(Instrumento):
    def tocar(self):
        print("Bateria: Tum dum tss! Ritmo forte e marcante.")

class Piano(Instrumento):
    def tocar(self):
        print("Piano: plim plum plamm... Melodia clássica e elegante.")

orquestra = [Violao(), Bateria(), Piano()]

for instrumento in orquestra:
    instrumento.tocar()