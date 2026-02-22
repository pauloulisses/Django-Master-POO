nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if nome == "Paulo" and idade == 22:
    print(f"Olá, {nome}, você tem {idade} anos.")
elif nome == "Chayenne" and idade == 26:
    print(f"Olá, {nome}, você tem {idade} anos.")
else:
    print("Você não está no banco de dados")