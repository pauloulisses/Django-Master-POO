# Operadores Lógicos

"""
Operador           definição
and               Retorna True se amabas as informações forem verdadeira
or                Retorna True se uma das afirmações for verdadeira
not               Retorna Falso se o resultado for verdadeiro
"""

# operador and
numero1 = 7
numero2 = 5
operacao = numero1 > 10 and numero2 < 20
print(operacao)

# operador or
number1 = 10
number2 = 20
operation = number1 > 50 or number2 < 50
print(operation)


# operador not
verdadeiro = True
falso = False
recebe = not verdadeiro and falso
print(recebe)