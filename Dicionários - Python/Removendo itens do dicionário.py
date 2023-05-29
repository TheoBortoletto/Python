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

### Removendo chaves e itens ###

print("\t Existem vários métodos para excluir uma chave ou um item de um dicionário: \n")

### pop() ###

print("\t Removendo item com 'pop()': \n")

print("Dicionário original", carDict)
carDict.pop("marca")
print("Dicionário com a chave 'marca' excluída: ", carDict, "\n")

### popitem() ###

print("\t Removendo item com 'popitem()': \n") # O popitem()método remove o último item                                                                     inserido (em versões anteriores a 3.7, um item aleatório                                                   é removido):
laptopDict.popitem()
print(laptopDict, "\n")

### del ###

print("\t Removendo item com 'del': \n")
del theoDict["nome"] # 'del' pode excluir um dicionário por inteiro ex: "del carDict"
print(theoDict, "\n")

### clear() -> esvazia o dicionário ###

print("Esvaziando dicionário com 'clear()': ")

carDict.clear()
print(carDict, "\n")
