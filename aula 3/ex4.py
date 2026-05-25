class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial  
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print("\n--- EXTRATO BANCÁRIO ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("------------------------\n")

conta_bruno = ContaBancaria("Bruno", 500.0)

conta_bruno.extrato()      
conta_bruno.depositar(200) 
conta_bruno.sacar(100)     
conta_bruno.sacar(800)     
conta_bruno.extrato()