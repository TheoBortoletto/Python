### Dicionários ###

carDict = {
  "marca": "Fiat",
  "modelo": "Uno",
  "ano": 2007
}

theoDict = {
  "nome": "Théo", 
  "altura": 1.90,
  "idade": 19
}

laptopDict = {
  "marca": "Lenovo",
  "processador": "intel",
  "ano": 2019
}

print("---------------------------------------------------------- \n")

print("\t Dicionários: \n")

print(carDict, "\n")
print(theoDict, "\n")
print(laptopDict, "\n")

print("---------------------------------------------------------- \n")

### Mudar valores ###

print("\t Alterando o valor da chave 'ano': \n")

print("Dicionário com valor da chave 'ano' antigo: ", carDict["ano"])

carDict["ano"] = 2010 # Mudando o valor da chave 'ano'

print("Dicionário com o valor da chave 'ano' atualizado: ", carDict["ano"], "\n")

### Mudando valor com o método 'update()' ###

print("\t Mudando valores de chaves usanod 'update()': \n")

print("Dicionário com os valores das chaves antigo: ", carDict)

carDict.update({"marca": "Honda"}) #Alterando valor da chave 'marca'
carDict.update({"modelo": "City"}) # #Alterando valor da chave 'modelo'

print("Dicionário com os valores de chaves atualizados: ", carDict, "\n")