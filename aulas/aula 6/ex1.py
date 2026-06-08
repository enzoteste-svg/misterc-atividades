class Funcionario:
    def calcular_salario(self):
        return 0

class Vendedor(Funcionario):
    def __init__(self, salario_fixo, comissao):
        self.salario_fixo = salario_fixo
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_fixo + self.comissao

class Gerente(Funcionario):
    def __init__(self, salario_fixo, bonus):
        self.salario_fixo = salario_fixo
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_fixo + self.bonus

vendedor = Vendedor(2000.0, 800.0)
gerente = Gerente(5000.0, 2500.0)

print(f"Salário do Vendedor: R$ {vendedor.calcular_salario():.1f}")
print(f"Salário do Gerente: R$ {gerente.calcular_salario():.1f}")