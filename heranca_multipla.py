class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emeitir_som(self):
        pass


class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando"
    

class Morcego(Mamifero, Ave):
    def emeitir_som(self):
        return "Morcegos emitem sons ultrassonicos"
    
morcego = Morcego(nome="Batman")


#Acessando metodos da classe base "Animal"

print("nome do morcego", morcego.nome)
print("som do morcego", morcego.emeitir_som())


# Acessando metodos das classses "mamifero" e "Ave"

print("Morcego amamemntando", morcego.amamentar())
print("Morcego voando", morcego.voar())
