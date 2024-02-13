# Crie uma tupla preenchida
# com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         "Cruzeiro", 'Flamengo', "Vasco", "Chapecoense",
         'Atlético', "Botafogo", "Atlético-PR", 'Bahia',
         'São Paulo', 'Fluminese', 'Sport Recife',
         "EC Vitória", "Coritiba", "Avai", "Ponte Preta",
         "Atlético-GO")

print(f"Lista de times do Brasileirão: {times}")
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
