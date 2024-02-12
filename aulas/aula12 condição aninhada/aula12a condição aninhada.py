nome = str(input('Qual é o seu nome? '))

if nome == 'Gustavo':
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "paulo":
    print("Seu nome é bem polular no Brasil")
elif nome in "Ana Cláudia Jéssica juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal!")
print(f"Tenha um bom dia, {nome}!")