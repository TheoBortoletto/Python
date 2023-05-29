### Dicionários ###

carDict = {
  "marca": "Volkswagen",
  "modelo": "Fusca",
  "ano": 1964
}

laptopDict = {
  "marca": "Vaio",
  "processador": "Intel",
  "ano": 2020
}

theoDict = {
  "nome": "Théo",
  "idade": 19,
  "altura": '1.90m'
}

print("-------------------------------------------------------- \n")

print("\t Dicionários: \n")

print(carDict, "\n")
print(laptopDict, "\n")
print(theoDict, "\n")

print("-------------------------------------------------------- \n")

### Loop de dicionários ###

print("\t Percorrer um dicionário e imprimir os nomes das chaves usando um 'for()': \n") 

for x in carDict:
  print(x, "\n")

print("\t Percorrer e imprimir os valores das chaves do dicionário: \n")

for y in carDict:
  print(carDict[y], "\n")

print("\t Usando 'values()' pra retornar valores de um dicionário: \n")

for z in theoDict.values():
  print(z, "\n")

print("\t Usando 'keys()' para retornar as chaves de um dicionário: \n")

for k in theoDict:
  print(k, "\n")

print("\t Usando 'items()' com com um 'for' para percorrer chaves e valores: \n")

for i, j in laptopDict.items():
  print(i,j, "\n")