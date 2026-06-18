class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self._nome = nome
        self._matricula = matricula
        self._salario_fixo = 0.0 
        self.set_salario_fixo(salario_fixo)

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_matricula(self):
        return self._matricula

    def set_matricula(self, matricula):
        self._matricula = matricula

    def get_salario_fixo(self):
        return self._salario_fixo

    def set_salario_fixo(self, valor):
        if valor < 0:
            print(f"Aviso: Salário negativo para {self._nome} não é permitido. Zerando o valor.")
            self._salario_fixo = 0.0
        else:
            self._salario_fixo = float(valor)

    def calcular_salario(self):
        return self._salario_fixo

    def exibir(self):
        pass


class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()

    def exibir(self):
        salario = self.calcular_salario()
        print(f"Nome : {self.get_nome()} Matricula : {self.get_matricula()} Tipo : CLT Salario : R$ {salario:.2f}")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, total_vendas):
        super().__init__(nome, matricula, salario_fixo)
        self._total_vendas = float(total_vendas)

    def get_total_vendas(self):
        return self._total_vendas

    def set_total_vendas(self, valor):
        if valor >= 0:
            self._total_vendas = float(valor)

    def calcular_salario(self):
        comissao = self._total_vendas * 0.10
        return self.get_salario_fixo() + comissao

    def exibir(self):
        salario = self.calcular_salario()
        print(f"Nome : {self.get_nome()} Matricula : {self.get_matricula()} Tipo : Vendedor Salario : R$ {salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)
        self._bonus = 1500.00

    def calcular_salario(self):
        return self.get_salario_fixo() + self._bonus

    def exibir(self):
        salario = self.calcular_salario()
        print(f"Nome : {self.get_nome()} Matricula : {self.get_matricula()} Tipo : Gerente Salario : R$ {salario:.2f}")


goes = CLT("Goés", "001", 30.50)
dambros = Vendedor("Dambros", "002", 2069.00, 12000.00)
vitoria = Gerente("Vitoria", "003", 5267.00)
pyetro = Gerente("Pyetro", "004", 6600.00)

lista_funcionarios = [goes, dambros, pyetro, vitoria]

print("-" * 65)
print("SISTEMA DE FOLHA DE PAGAMENTO")
print("-" * 65)

for func in lista_funcionarios:
    func.exibir()
    
print("-" * 65)
