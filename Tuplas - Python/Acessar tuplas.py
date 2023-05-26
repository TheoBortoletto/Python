### Tuplas ###

fruitTuple = ("maçã", "pêra", "abacaxi", "tomate", "cereja", "manga", "kiwi", "melão")
carsTuple = ("Honda", "Fiat", "Tesla", "Volvo", "BMW")

print("--------------------------------------------------- \n")
print("\t Tuplas: \n")

print(carsTuple, "\n")
print(fruitTuple, "\n")

print("--------------------------------------------------- \n")


### Acessar itens da tupla ###

print("\t Acessando um item de uma tupla: \n")
print(fruitTuple[2], "\n") ### Note o uso do colchetes "[]", para acessar um item da tupla

### Acessar itens da tupla com indexação negativa ###

print("\t Acessando um item da tupla mas agora acom indexação negativa: \n")
print(fruitTuple[-1], "\n") ### "[-1]" refere-se ao último item, "[-2]" se refere so penútimo item, etc.

### Acessar itens da tupla com intervalos ###

print("\t Acessando itens de uma tupla com intervalos: \n")
print(fruitTuple[2:5], "\n") ### Retorna do item 3 ao item 5

print("\t Acessar itens de uma tupla com intervalos mas sem usar o valor inicial: \n")
print(fruitTuple[:5], "\n") ### Retorna do primeiro item ao quinto item

print("\t Acessar itens de uma tupla com intervalos mas sem usar o valor final: \n")
print(fruitTuple[2:], "\n") ### Retorna o item 3 até o final

### Acessar itens da tupla com intervalos de indexação negativa ###

print("\t Acessar itens da tupla com intervalos de indexação negativa: \n")
print(fruitTuple[-4:-1], "\n") ### Este exemplo retorna os itens do índice -4 (incluído) ao índice -1 (excluído)

### Verificar se um item existe ###

print("\t Checar lista e verificar se o item existe: \n")
print("\t Cheque se nesta tupla:", carsTuple,"existe 'Tesla' \n")

if "Tesla" in carsTuple:
  print("Existe 'Tesla' nessa tupla")
else:
  print("Não existe 'Tesla' nessa tupla")
