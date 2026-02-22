# Inicia o contador em 0
contador = 0

# Enquanto o contador for menor que 11 (vai até 10)
while contador < 11:

    # Incrementa o contador de 1 em 1
    contador += 1

    # Se o contador for igual a 3 pula ele e continua aprtir do 4
    if contador == 3:
        # Pula essa volta do loop e volta para o while
        continue

    # Mostra o valor do contador (menos o 3)
    print(contador)



