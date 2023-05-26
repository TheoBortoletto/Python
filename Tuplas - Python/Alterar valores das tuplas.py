### Tuplas ###

fruitsTuple = ("maçã", "banana", "cereja")
carsTuple = ("Volvo", "Tesla", "Honda")
oneItemTuple = ("laranja",)
peopleTuple = ("Théo", "Alan", "Larissa", "Beatriz", "Lívia")
print("------------------------------------------------------------ \n")

print("\t Tuplas: \n")
print(fruitsTuple, "\n")
print(carsTuple, "\n")
print(oneItemTuple, "\n")
print(peopleTuple, "\n")

print("------------------------------------------------------------ \n")

### Alterar valores de Tuplas ###

''' 
As tuplas são imutáveis, o que significa que você não pode alterar, adicionar ou remover itens depois que a tupla é criada.
Mas existem algumas soluções alternativas.
'''

print("\t Alterar o valor de uma Tupla transformando ela em lista: \n")

newValueFruit = list(fruitsTuple) # Converto a tupla para lista
newValueFruit[1] = "MUDEI O VALOR" # Mudo o valor na lista
fruitTuple = tuple(newValueFruit) # Converto a lista em Tupla

print(fruitTuple, "\n")

### Adicionar itens na Tupla ###

print("\t Adicionar itens na Tupla: \n")

newValueCars = list(carsTuple) # Converto a tupla para lista
newValueCars.append("NOVO ITEM") # Adiciono um item na lista (que era uma tupla)
carsTuple = tuple(newValueCars) # Converto a lista para tupla

print(carsTuple, "\n")

### Adicionar tupla a uma Tupla ###

print("\t Adicionar Tupla a uma Tupla: \n")

fruitsTuple += oneItemTuple

print(fruitsTuple, "\n")

### Remover itens de uma Tupla ###

print("\t Remover itens de uma tupla: \n")

removeItemPeople = list(peopleTuple)
removeItemPeople.remove("Théo")
peopleTuple = tuple(removeItemPeople)

print(peopleTuple, "\n")

print("\t Excluir tupla: \n")

#del fruitsTuple
print(fruitsTuple)





