class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if len(nome.strip()) > 0:
            self.__nome = nome
        else:
            print("Erro: O nome não pode ser vazio.")

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("Erro: A idade deve estar entre 0 e 120.")

    def apresentar(self):
        print(f"Nome: {self.__nome} | Idade: {self.__idade} anos")

pessoa1 = Pessoa("Carlos", 25)
pessoa1.apresentar()

pessoa1.set_nome("")       
pessoa1.set_idade(150)    
pessoa1.set_idade(30)      
pessoa1.apresentar()