# formatar um nome com alinhamento

nome = input("Qual é seu nome? ")
print(f"Prazer em te conhecer {nome:>10}")  # o nome ficara a direita exemplo  ->  "Prazer em te conhecer     carlos"
print(f"Prazer em te conhecer {nome:<10}")  # o nome ficara a esquerda exemplo -> "Prazer em te conhecer carlos    "
print(f"Prazer em te conhecer {nome:^10}")  # o nome ficara centralizado       -> "Prazer em te conhecer   carlos  "

print(f"Prazer em te conhecer {nome:=>10}")  # o nome ficara a direita         -> "Prazer em te conhecer ====carlos"
print(f"Prazer em te conhecer {nome:=<10}")  # o nome ficara a esquerda        -> "Prazer em te conhecer carlos===="
print(f"Prazer em te conhecer {nome:=^10}")  # o nome ficara no centralizado   -> "Prazer em te conhecer ==carlos=="
