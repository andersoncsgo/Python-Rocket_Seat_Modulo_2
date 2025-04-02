# @classmethod
# @staticmethod

class Minhaclasse:
    valor = 10 # atributo da classe
    def __init__(self, nome):
        self.nome = nome # Atributo da instancia

    # Requer uma instancia para ser chamado
    def metodo_instancia(self):
        return f"metodo de instacia chamda para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"metodo de classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Metodo estatico chamado"
    
obj = Minhaclasse(nome="classe exemplo")
print(obj.metodo_instancia())
print(Minhaclasse.valor)
print(Minhaclasse.metodo_classe())
print(Minhaclasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "toyota, corolla, 2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\n Ano: {carro1.ano}")

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a=10, b=15))
