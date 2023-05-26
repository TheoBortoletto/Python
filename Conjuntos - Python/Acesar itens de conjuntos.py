### Conjuntos ###

fruitSet = {"maçã", "pêra", "laranja", "cereja"}
carsSet = {"tesla", "honda", "volvo", "fiat"}
nameSet = {"Théo", "Larissa", "Alan", "Beatriz", "Lívia"}

print("--------------------------------------------------------- \n")

print("\t Conjuntos: \n")
print(fruitSet, "\n")
print(carsSet, "\n")
print(nameSet, "\n")

print("--------------------------------------------------------- \n")

### Percorrer um conjunto usando um 'for' ###

print("\t Percorrer um conjunto usando um 'for': \n")

for x in fruitSet:
  print(x, "\n")

### Verificar se há um item em um conjunto ###

print("\t Verificar se há um item em um conjunto: \n")
print("\t\t Verificar se o item 'Théo' está no conjunto 'nameSet': \n")
print(nameSet, "\n")

print("Théo" in nameSet, "\n")