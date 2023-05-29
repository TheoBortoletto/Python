### Matrizes ###
print("\t --- Matrizes: --- \n")

print("\t --- Criar Matriz: --- \n")

###

cars = ["Ford", "Volvo", "BMW"]
print(cars, "\n")

# Uma matriz é uma variável especial, que pode conter mais de um valor por vez.

# Modififcar valor de um item da matriz

print("\t --- Modificar um item da matriz: --- \n")

people = ["Alan", "Lívia", "Beatriz", "Larissa", "Théo"]
print(people, "\n")

people[4] = "Henrique"  #Não será mais Théo, será Henrique agora
print(people, "\n")

# Ver o comprimento de uma matriz 

print("\t --- Comprimento de uma matriz: --- \n")

tech = ["laptop", "mice", "monitor", "keyboard", "smartphone"]
print(tech, "\n")

lenTech = len(tech)
print("O comprimento da matriz é:",lenTech, "\n")

# Elementos de matriz em loop

print("\t --- Percorrendo matriz: --- \n")

num = [1, 3, 4, 6, 7, 33, 55]
print(num, "\n")

for x in num:
  print(x)

# Adicionando elemetos na matriz 'append()'

print("\t --- Adicionando elementos na matriz: --- \n")

books = ["books1", "books2", "books3"]
print(books, "\n")

books.append("book4")
print(books, "\n")

# Removendo elemetos na matriz 'pop()' ou 'remove()'

print("\t --- Removendo elementos da matriz: --- \n")

print("\t Usando o 'pop()': \n")

random = ["oi", "olá", "saudações"]
print(random, "\n")

random.pop(1) # Excluiu o segundo elemento da matriz
print(random, "\n")

#

print("\t Usando o 'remove()': \n")

random2 = ["aleatório", "Olá", "hello World", "random"]
print(random2, "\n")

random2.remove("hello World")
print(random2, "\n")
