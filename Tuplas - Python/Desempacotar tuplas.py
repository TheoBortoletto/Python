### Tuplas ###

fruitsTuple = ("maçã", "banana", "pêra")
carsTuple = ("Volvo", "Tesla", "Honda")
oneItemTuple = ("laranja",)
peopleTuple = ("Théo", "Alan", "Larissa", "Beatriz", "Lívia")
randomTuple = ("céu", "mouse", "laptop", "teclado", "elefante")

print("------------------------------------------------------------ \n")

print("\t Tuplas: \n")
print(fruitsTuple, "\n")
print(carsTuple, "\n")
print(oneItemTuple, "\n")
print(peopleTuple, "\n")
print(randomTuple, "\n")

print("------------------------------------------------------------ \n")

### Quando criamos uma tupla, normalmente atribuímos valores a ela. Isso é chamado de "empacotar" uma tupla ###

### Desempacotando uma Tupla ###

print("\t Desempacotando uma tupla \n")
(vermelho, amarelo, verde) = fruitsTuple

print(vermelho, "\n")
print(amarelo, "\n")
print(verde, "\n")

### Usando o '*', Se o número de variáveis for menor que o número de valores, você pode adicionar um *ao nome da variável e os valores serão atribuídos à variável como uma lista ###

print("\t Usando o '*': \n")

(T, A,  *M) = peopleTuple

print(T)
print(A)
print(M)

### Se o asterisco for adicionado a outro nome de variável diferente do anterior, o Python atribuirá valores à variável até que o número de valores restantes corresponda ao número de variáveis restantes. ###

print("\t Usando o '*' para mais de um item: \n")

(azul, *preto, cinza) = randomTuple

print(azul, "\n")
print(preto, "\n")
print(cinza, "\n")