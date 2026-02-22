"""
Polimorfismo de interfave
"""

# =====================================
# CLASSE BASE (FORMA)
# =====================================
class Forma():

    # método que será sobrescrito pelas classes filhas
    # aqui não faz nada, só define que toda forma terá area()
    def area(self):
        pass


# =====================================
# CLASSE FILHA (QUADRADO)
# HERDA de Forma
# =====================================
class Quadrado(Forma):

    # método construtor
    # executa automaticamente quando criamos o objeto
    def __init__(self, lado):
        # self.lado guarda o valor do lado do quadrado
        self.lado = lado

    # sobrescrevendo (override) o método area da classe Forma
    def area(self):
        # fórmula da área do quadrado = lado²
        return self.lado ** 2


# =====================================
# CRIANDO OBJETO
# =====================================

# cria um quadrado com lado = 5
quadrado = Quadrado(5)

# chama o método area() do objeto
area_quadrado = quadrado.area()

# imprime o resultado da área
print(area_quadrado)






       