### Conjuntos ###

fruitSet = {"maçã", "pêra", "laranja", "cereja"}
carsSet = {"tesla", "honda", "volvo", "fiat"}
nameSet = {"Théo", "Larissa", "Alan", "Beatriz", "Lívia"}
updateSet = {1, 2, 3, 4}

print("--------------------------------------------------------- \n")

print("\t Conjuntos: \n")
print(fruitSet, "\n")
print(carsSet, "\n")
print(nameSet, "\n")
print(updateSet, "\n")

print("--------------------------------------------------------- \n")

### Adicionar itens ###

print("\t Adicionar itens em conjuntos: \n")

fruitSet.add("abacate")
print(fruitSet, "\n")

### Adicionar itens de um conjunto ao conjunto atual ###
 
print("\t Adicionar itens de um conjunto ao conjunto atual: \n")

fruitSet.update(updateSet)
print(fruitSet, "\n")

### Adicionar qualquer iterável. O objeto no update()método não precisa ser um conjunto, pode ser qualquer objeto iterável (tuplas, listas, dicionários etc.).  ###

print("\t Adicionar itens de uma lista a um comjunto \n")

fruitList = ["kiwi", "melancia"]

carsSet.update(fruitList)
print(carsSet, "\n")