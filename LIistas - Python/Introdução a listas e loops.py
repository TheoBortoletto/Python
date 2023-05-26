print("\t Imprimir itens da lista: \n")
### Lista com funções de remover e adicionar ###

print("\t Lista extendida de marcas de carro e roupas: \n")

myCarsList = ["Volvo", "Fiat", "Bmw"]
brandList = ["Siberian", "Crawford", "Valdac"]
myCarsList.extend(brandList) #estender lista
#myCarsList.append("chevrolet")
#myCarsList.insert(1, "chevrolet")
#brandList.remove("Crawford")
#myCarsList.pop(1)
print(myCarsList)
print("\n")

computersList = ["Dell", "Acer", "Lenovo"]
print("\t Lista de marca de compuutadores: \n")
print(computersList) 
print("\n")


listPeople = ["Alan", "Beatriz", "Larissa", "Lívia", "Théo"]
print("\t Lista de pessoas \n")
print(listPeople)
print("\n")

### Imprimir todos os itens da lista, um por um: ###

print("\t Imprimir intens da lista um por um: \n")
for x in myCarsList:
  print(x)
print("\n")


### Imprimir todos os itens da lista referindo-se ao seu número de índice: ###

print("\t Imprimir todos os itens da lista referindo-se ao seu número de índice: \n")
for i in range(len(computersList)):
  print(computersList[i])
print("\n")  


### Usando um loo while ###

print("\t Usando um loop com while: \n")

i = 0
while i < len(listPeople):
  print(listPeople[i])
  i+=1 #(i = i + 1)
print("\n")

### Fazendo loop usando uma sintaxe curta ###

print("\t Fazendo um loop praa imprimir itens da lista usando sintaxe curta \n")

[print(x) for x in listPeople]
