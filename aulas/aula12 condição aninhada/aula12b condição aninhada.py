nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print(f"Seu nome contem espaços")
    else:
        print(f"Seu nome não contém espaços")

    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]} ")
    print(f"A ultima letra do seu nome é {nome[-1]} ")

else:
    print("Desculpe, você deixou campos vazios")