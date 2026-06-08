class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(f"Funcionário: {self.nome} | Salário Base: R$ {self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus

gerente1 = Gerente("Rodrigo", 5000.0, 1500.0)
gerente1.exibir()
print(f"Salário Total (com bônus): R$ {gerente1.salario_total():.2f}")