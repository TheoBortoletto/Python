### Listas ###

print(
  "-------------------------------------------------------------------- \n")
print("\t Listas: \n")

listNames = ["Jaime", "Larissa", "Théo", "Alan", "André", "Beatriz", "Lívia"]
listNum = [20, 45, 50, 5, 35, 15, 10, 25, 30, 40]
listNum2 = [1, 35, 42, 34, 86, 69, 84, 7]
listFruits = ["Laranja", "Maçã", "abacate", "Abacate", "banana", "Coco"]

print(listNames)
print("\n")
print(listNum)
print("\n")
print(listNum2)
print("\n")
print(listFruits)
print("\n")

print("--------------------------------------------------------------------")
print("\n")

### Ordenar lista em ordem alfabética ###

print("\t Lista ordenada em ordem alfabética: \n")
listNames.sort()
print(listNames)
print("\n")

print("\t Lista ordenada em ordem alfabética decrescente: \n")
listNames.sort(reverse=True)
print(listNames)
print("\n")

print(
  "\t Lista ordenada em ordem alfabética que diferencia letras maiúscula e minúscula: \n"
)
listFruits.sort()
print(listFruits)
print("\n")

print(
  "\t Lista ordenada em ordem alfabética que não diferencia letras maiúculas e minúsculas: \n"
)
listFruits.sort(key=str.lower)
print(listFruits)
print("\n")

print("\t Inverter ordem da lista independentemente do alfabeto: \n")
listFruits.reverse()
print(listFruits)
print("\n")

print(
  "-------------------------------------------------------------------- \n")

### Ordenar lista em ordem numérica ###

print("\t Lista ordenada em ordem numérica crescente: \n")
listNum.sort()
print(listNum)
print("\n")

print("\t Lista ordenada em ordem numérica decrescente: \n")
listNum.sort(reverse=True)
print(listNum)
print("\n")

### Classificar lista com base no número que esta mais próximo do número requisitado para depois continuar com a ordenação da lista ###

print("\t Classificar lista que esta mais próximo do núemro requisitado: \n")


def orderfunc(n):
  return abs(n - 35)  # 'abs' retorna o valor absoluto


listNum2.sort(key=orderfunc)
print(listNum2)
print("\n")

print(
  "-------------------------------------------------------------------- \n")
