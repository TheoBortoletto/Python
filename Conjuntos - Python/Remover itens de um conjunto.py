### Conjuntos ###

fruitSet = {"maçã", "pêra", "laranja", "cereja"}
carsSet = {"tesla", "honda", "volvo", "fiat"}
nameSet = {"Théo", "Larissa", "Alan", "Beatriz", "Lívia", "Fábio"}
techSet = {"laptop", "desktop", "cellphone", "mouse"}
numSet = {1, 2, 3, 54, 784, 734}

print("--------------------------------------------------------- \n")

print("\t Conjuntos: \n")
print(fruitSet, "\n")
print(carsSet, "\n")
print(nameSet, "\n")
print(techSet, "\n")
print(numSet, "\n")

print("--------------------------------------------------------- \n")

### Remover item do conjunto ### 

print("\t Remover item de um conjunto: \n")

nameSet.remove("Fábio") # Caso o item a ser removido não exista, remove() gerará um erro.
                        # Caso o item a ser removido não exista, discard() NÃO gerará erro.
print(nameSet, "\n")

### Usando o 'pop()' pra remover um item aleatório ###

print("\t Usando o 'pop()' pra remover um item aleatório: \n")

x = fruitSet.pop()
print("o item", '{', x,'}' " foi aleatóreamente removido do conjunto: \n")
print(fruitSet, "\n")

### Usando o 'clear()' para esvaziar o conjunto ###

print("\t Usando o 'clear()' para esvaziar conjuntos: \n")

techSet.clear()
print(techSet, "\n")

### Usando o 'del()' para excluir um conjunto completamente ###

print("\t Usando o 'del()' para excluir um conjunto completamente: \n")

del numSet
print(numSet, "\n") # Retornará um erro pois o conjunto não existe mais no escopo 
