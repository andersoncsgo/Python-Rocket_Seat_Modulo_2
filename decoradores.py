def meu_decorador(func):
    def wrapper():
     print("antes da funcao ser chamada")
     func()
     print("depois da funcao ser chamda")
    return wrapper
    
@meu_decorador    
def minha_funcao():
    print("minha funcao foi chamada")

minha_funcao()


class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self) -> any:
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")


@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao()  
