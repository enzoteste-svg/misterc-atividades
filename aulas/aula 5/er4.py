class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"Aluno: {self.nome} Idade: {self.idade} Matrícula: {self.matricula}")

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(f"Professor: {self.nome} Idade: {self.idade} Salário: R$ {self.salario:.2f}")

usuarios_escola = [
    Aluno("Lucas", 16, "202401ABC"),
    Professor("Beatriz", 35, 4200.0),
    Aluno("Mariana", 17, "202402XYZ"),
    Professor("Fernando", 48, 5100.0)
]

for pessoa in usuarios_escola:
    pessoa.apresentar()