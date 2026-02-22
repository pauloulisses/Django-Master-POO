# Objeto - Celular

# propriedades celular 
# marca: Nokia
# modelo: Tijolão
# cor: Azul
# tem camera? não
# bateria: infinita

# Funções
# fazer ligação
# jogar cobrinha
# despertador

class Celular:
    # propriedades
    marca = "nokia"
    modelo = "tijolão"
    cor = "azul"
    tem_camera = False
    bateria = "infinita"

    # funções
    def fazer_ligação(self):
        print('Fazendo ligação...')
    def jogar_cobrinha(self):
        print('Jogando cobrinha...')
    def despertador(self):
        print('Despertando...') 

# Instancia da class celular()
Celular = Celular()  

# chmando as proriedades da class celular
print(Celular.marca)
print(Celular.modelo)
print(Celular.cor)  
print(Celular.tem_camera)
print(Celular.bateria)  


             