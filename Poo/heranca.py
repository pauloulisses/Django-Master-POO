# HERANÇA
class Carro:
   # propriedades carro
   numeros_rodas = 4
   quantidade_passageiros = 5


   # funções do carro
   def acelarar(self):
      print('Acelerando...')

   def frear(self):
      print('Freando...')

   def buzinar(self):
      print('Buzinando...')   
 
# instanciando
carro = Carro()
carro.acelarar()
carro.buzinar()
carro.frear()

# HERANÇA HERDANDO propriedades e funções DA CLASS PRINCIPAL
class Uno(Carro): # instacia tudo da classe CARRO em parentese ( )
   # propriedades 
   modelo = 'Uno'
   marca = 'Fiat'
   ano = 1992
   
uno = Uno()
uno.frear()
uno.buzinar()   
print(uno.marca)
print(uno.modelo)
print(uno.ano)