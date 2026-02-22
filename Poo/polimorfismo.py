"""
Polimorfismo - permitir que class diferentes que herdam
da mesma class possam ter propriedades e metos e funções, com mesmo nome mais que executam coisas diferentes
"""

# class pai 
class Animal:
    # função da clss Animal
    def emitir_som(self):
        print('Qualquer som...')


# class cachorro herda parametros da clss (Animal)
class Cachorro(Animal):
    # subcreve a função emitir som que herda de Animal
    def emitir_som(self):
        print('Au Au!')


# class gato herda paramentros da clss (Animal)
class Gato(Animal):
    # subcreve a função emitir som que herda de Animal
    def emitir_som(self):
        print('Miau!')

class Vaca(Animal):
    def emitir_som(self):
        print('muuu...')
# Intânciando
cachorro = Cachorro()
cachorro.emitir_som()

# Instanciando 
gato = Gato()
gato.emitir_som()

# Instanciando
vaca = Vaca()
vaca.emitir_som()