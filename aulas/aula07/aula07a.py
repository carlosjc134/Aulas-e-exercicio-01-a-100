# formatar um nome com alinhamento

# nome = input("Qual é seu nome? ")
# print(f"Prazer em te conhecer {nome:>10}")  # o nome ficara a direita exemplo  ->  "Prazer em te conhecer     carlos"
# print(f"Prazer em te conhecer {nome:<10}")  # o nome ficara a esquerda exemplo -> "Prazer em te conhecer carlos    "
# print(f"Prazer em te conhecer {nome:^10}")  # o nome ficara centralizado       -> "Prazer em te conhecer   carlos  "
#
# print(f"Prazer em te conhecer {nome:=>10}")  # o nome ficara a direita         -> "Prazer em te conhecer ====carlos"
# print(f"Prazer em te conhecer {nome:=<10}")  # o nome ficara a esquerda        -> "Prazer em te conhecer carlos===="
# print(f"Prazer em te conhecer {nome:=^10}")  # o nome ficara no centralizado   -> "Prazer em te conhecer ==carlos=="

print(f"R$ {1.59}")
print(f"R$ {1.59:f}")
print(f"R$ {1.59:.2f}")
print(f"R$ {1.5:.2f}")
print(f"R$ {1234.5:.2f}")
print("=--==-=-=-=-=-=-=--=")

print(f"R$ {1.59:07.2f}")
print(f"R$ {1.59:07.2f}")
print(f"R$ {1.5:07.2f}")
print(f"R$ {1234.5:07.2f}")
print("=--==-=-=-=-=-=-=--=")

print(f"R$ {4.5:07.2f}")  # float
print(f"R$ {4:07d}")  # inteiro
print(f"R$ {4:7d}")  # inteiro
print("=--==-=-=-=-=-=-=--=")

print(f"Data {9:2d}/{4:2d}")
print(f"Data {9:02d}/{4:02d}")
print(f"Data {19:02d}/{11:02d}")


