### Ttuplas ###

carsTuple = ("honda", "tesla", "volvo", "fiat")
fruitTuple = ("maçã", "laranja", "abacate", "cereja")
peopleTuple = ("Alan", "Théo", "Larissa", "Lívia", "Beatriz")

print("-------------------------------------------------------------, \n")

print("TUPLAS: \n")

print(carsTuple, "\n")
print(fruitTuple, "\n")
print(peopleTuple, "\n")

print("-------------------------------------------------------------, \n")

### Percorrer uma Tupla ###

print("\t Percorrer uma Tupla: \n") # Usando o 'for()'

for x in peopleTuple:
  print("\t", x)
print("\n")

### Percorrer os números de índice ###

print("\t Percorrer os números de índice: \n")

for i in range(len(fruitTuple)):
  print("\t", fruitTuple[i])
print("\n")
  
### Usando um loop 'while' ###

print("\t Usando while pra percorrer Tuplas: \n")

z = 0
while z < len(carsTuple):
  print("\t", carsTuple[z])
  z = z + 1
print("\n")