### Listas ###

listPeople = ["Alan", "Beatriz", "Larissa", "Lívia", "Théo"]
listCars = ["Fiat", "BMW", "Chevrolet", "Volvo"]
listFruits = ["Apple", "Orange", "Peneapple", "Banana"]

print("\t Listas: \n")

print("-----------------------------------------------------")
print(listPeople)
print(listCars)
print(listFruits)
print("-----------------------------------------------------")

print("\n")

### Exemplo de lista contendo apenas palavras com tais letras ###

newList = [
]  # Lista nova que sera usada para pegar as palavras que contenham tais letras

for x in listFruits:
  if "n" in x:
    newList.append(x)

print('\t Lista de Frutas que só tenham a letra "n": \n')
print(newList)
print("\n")

### Algoritmo de cima com compreensão de lista (em apenas uma linha) ###

print('\t lista de pessoas que não possuem a letra "o" no nome: \n')
newList2 = [x for x in listPeople if "o" not in x]
print(newList2)
print("\n")

### Imprimir apenas itens que não sejam o que você não quer ###

print('\t Lista dos carros que não seja "BMW": \n')
newList3 = [x for x in listCars if x != "BMW"]
print(newList3)
print("\n")

### Deixar a lista com os caractéres em 'CAPS LOCK' ###

print("\t Imprimir lista em 'CAPS LOCK': \n")
newListUpercase = [x.upper() for x in listPeople]
print(newListUpercase)
print("\n")

### Colocar novos valores em una lista ###

print("\t Lista com novos vlores: \n")
newListValues = ["New Value" for x in listCars]
print(newListValues)
print("\n")

### Retornar outro valor ao invés do valor original em uma lista ###

print("\t Retornar outro valor ao invés do valor original: \n")

newListValue2 = [x if x != "Fiat" else "Tesla" for x in listCars]
print(newListValue2)
print("\n")
