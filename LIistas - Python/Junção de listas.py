### Listas ###

listNum = [1, 2, 3, 4, 5]
listStr = ["a", "b", "d", "e", "f"]
listName = ["Théo", "Larissa", "Lívia", "Beatriz", "Alan"]
listCars = ["Fiat", "Volvo", "Tesla", "Honda"]
list1to5 = [1, 2, 3, 4, 5]
list6to10 = [6, 7, 8, 9, 10]

print("---------------------------------------------------- \n")
print("\t Listas: \n")
print(listNum)
print("\n")
print(listStr)
print("\n")
print(listName)
print("\n")
print(listCars)
print("\n")
print(list1to5)
print("\n")
print(list6to10)
print("\n")
print("---------------------------------------------------- \n")

### Juntar duas listas ###

print("\t Juntar duas listas: \n")

listNumSrt = listNum + listStr
print(listNumSrt)
print("\n")

print("\t Juntar duas listas, mas dessa vez anexando uma na outra: \n")

for x in listCars:
  listName.append(x)

print(listName)
print("\n")

print("\t Juntar duas listas pelo método extend(), cujo objetivo é adicionar elementos de uma lista para outra lista : \n")

list1to5.extend(list6to10)
print(list1to5)
print("\n")

                  