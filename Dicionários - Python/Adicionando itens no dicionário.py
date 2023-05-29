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


### Adicionando itens ###

print("\t Adicionando itens nos dicionários \n")

carDict["cor"] = "Azul"
print(carDict, "\n")

print("\t Usando o 'update()': \n")

laptopDict.update({"estado": "Usado"})

print(laptopDict, "\n")