#Exemplo
class Pessoa:
    # Método construtor (inicializa os atributos da classe)
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade

    # Método para exibir informações da pessoa
    def mostrar_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Carlos", 25)
pessoa1.mostrar_info()  # Saída: Nome: Carlos, Idade: 25
