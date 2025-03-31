# POO

# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Ola, meu nome e {self.nome} e eu tenho {self.idade} anos."
        
# Obejetos
pessoa1 = Pessoa("Alice", 30)
print("Nome:", pessoa1.nome)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Rodrigo", idade="32")
mensagem = pessoa2.saudacao()
print(mensagem)
