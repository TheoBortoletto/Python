### Dicionários ###

carDict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1969
}

theoDict = {
  "nome": "Théo",
  "idade": 19,
  "dataNasc": 2003,
  "altura": "1.90m"
}

laptopDict = {
  "marca": "Vaio",
  "ano": 2020,
  "processador": "AMD"
}

print("---------------------------------------------------------------------------- \n")

print("\t Dicionários: \n")

print(carDict, "\n")
print(theoDict, "\n")
print(laptopDict, "\n")

print("---------------------------------------------------------------------------- \n")

### Copiar um dicionário ###

print("\t Copiar um dicionário, usando o método 'copy()': \n")

carCopyDict = carDict.copy()
print(carCopyDict, "\n")

print("\t Copiar um dicionário, usando o método 'dict()': \n")

theoCopyDict = dict(theoDict)
print(theoCopyDict, "\n")
