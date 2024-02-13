lanche = ["hamburguer", "suco", "pizza", "Pudim"]
print(lanche)  # mostrara -> ['hamburguer', 'suco', 'pizza', 'Pudim']

lanche[3] = "picole"  # a pizza pelo picole
print(lanche)  # mostrara -> ['hamburguer', 'suco', 'pizza', 'picole']


lanche.append("coque")  # adicionar itens na lista
print(lanche)  # mostrara -> ['hamburguer', 'suco', 'pizza', 'picole', 'coque']

lanche.insert(0, "batata")  # adicionar itens na numeração
print(lanche)  # mostrara -> ['batata', 'hamburguer', 'suco', 'pizza', 'picole', 'coque']

del lanche[3]  # apagar o item pizza na lista
print(lanche)  # mostrara -> ['batata', 'hamburguer', 'suco', 'picole', 'coque']

lanche.pop()  # apagar o ultimo item da lista
print(lanche)  # mostrara -> ['batata', 'hamburguer', 'suco', 'coque']

lanche.remove("suco")  # apagar o item da lista
print(lanche)  # mostrara -> ['batata', 'hamburguer', 'picole']
