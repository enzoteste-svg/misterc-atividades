class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print(f"Titular: {self.__titular} | Saldo Atual: R$ {self.__saldo:.2f}")

conta = ContaBancaria("Mariana")
conta.extrato()

conta.depositar(500.0)
conta.sacar(200.0)
conta.sacar(400.0)     
conta.depositar(-50)   
conta.extrato()