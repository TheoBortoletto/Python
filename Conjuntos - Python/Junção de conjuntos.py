### Conjuntos ###

fruitSet = {"maçã", "pêra", "laranja", "cereja"}
carsSet = {"tesla", "honda", "volvo", "fiat"}
nameSet = {"Théo", "Larissa", "Alan", "Beatriz", "Lívia"}
numSet = {1, 2, 3, 4, 5}
num2Set = {6, 7, 8, 9, 10}
w = {22, 33, 44, 55}
v = {22, 44, 66, 77}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
num3Set = {True, 31, 32, 33}
num4Set = {1, 2, 3}


print("--------------------------------------------------------- \n")

print("\t Conjuntos: \n")
print(fruitSet, "\n")
print(carsSet, "\n")
print(nameSet, "\n")
print(numSet, "\n")
print(num2Set, "\n")
print(w, "\n")
print(v, "\n")
print(x, "\n")
print(y, "\n")
print(num3Set, "\n")
print(num4Set, "\n")

print("--------------------------------------------------------- \n")

### Juntar dois conjuntos ###

print("\t Juntar doois conjuntos: \n")

nameCarSet = nameSet.union(carsSet)
print(nameCarSet, "\n")

### Usando 'update()', método que insere itens de um conjunto em outro ###

print("\t Usando o método 'update()': \n") # 'union()' e 'update()' excluirão itens duplicados

numSet.update(num2Set)
print(numSet, "\n")

### Método de interseção de conjuntos, manter no conjunto apenas os itens que estiverem em ambos os conjuntos ###

print("\t Interseção de conjuntos, imprimindo apenas os itens que existem em ambos os conjuntos (esse método mantém os itens que existem em 'x' e 'y'): \n")

x.intersection_update(y) # Método para interseção

print(x, "\n")

### Método 'intersection()' retornará um novo conjunto, que contém apenas os itens presentes em ambos os conjuntos. ###

print("\t Esse método retorna um conjunto que contenha os itens que existem noo conjunto 'w' e 'v' \n")

print(w, "\n")
print(v, "\n")

z = w.intersection(v)
print("\t Itens em comum que contém nos conjuntos acima:", z, "\n")

### Manter os itens que não estão presentes em ambos os conjuntos ###

print("\t Manter os itens que não estão presentes em ambos os conjuntos: \n")

x.symmetric_difference_update(y)
print(y, "\n")

### O symmetric_difference()método retornará um novo conjunto, que contém apenas os elementos que NÃO estão presentes em ambos os conjuntos. ###

print("\t Método que retornará um novo conjunto, que contém apenas os elementos que NÃO estão presentes em ambos os conjuntos: \n")

h = w.symmetric_difference(v)
print(h, "\n")

print("\t 'True' e '1' é considerado o mesmo valor: \n")

p = num3Set.symmetric_difference(num4Set)
print(p, "\n")

