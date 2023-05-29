### Dicionários ###

carDict = {
  "marca": "Fiat",
  "modelo": "Uno",
  "ano": 2007
}

theoDict = {
  "nome": "Théo", 
  "altura": "1.90m",
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

### Acessando itens ###

print("\t Acessando itens de um dicionário: \n")

x = carDict["marca"] #  Você pode acessar os itens de um dicionário referindo-se ao seu nome                           de chave, entre colchetes
print(x, "\n")

### Acessando itens pelo método 'get()' ###

print("\t Acessando itens pelo método 'get()': \n")

y = carDict.get("modelo")
print(y, "\n")

### Acessando as chaves de um dicionário ###

print("\t Obtendo as chaves de um dicionário: \n")

z = carDict.keys() # Esse método retornará uma lista de todas a chave do dicionário
print(z, "\n")

### Obtendo chaves do dicionário e alterando os seus valores ###

print("\t Adicionar um novo item de chave ao dicionário original: \n")

w = theoDict.keys()

print("Dicionário original:", w, "\n")  # Dicionário original (antes da mudança a seguir)

theoDict["anoNascimento"] = 2003  # Alterar valores de chaves também altera a lista de valores

print("Dicionário atualizado:", w, "\n")  # Dicionário atualizado

### Obtendo valores  ###

print("\t Obtendo valores de um dicionário (uma lista de valores sera retornada): \n")

k = laptopDict.values()
print(k, "\n")

### Obtendo valores do dicionario e alterando os seus valores ###

print("\t Alterando valores das chaves: \n")

print("Valor original: ",k, "\n") # Dicionário com valor original

laptopDict["marca"] = "Dell"

print("Valor alterado: ", k, "\n") # Dicionário com valor

### Otendo itens ###

print("\t Obtendo itens nos dicionários: \n")

r = theoDict.items()
print(r, "\n")

### Verificar se a chave existe ###

print("\t Verificar se a chave existe: \n")

if "modelo" in carDict:
  print("Sim, a chave 'modelo' existe nesse dicionário \n")
else:
  print("Não, a chave 'modelo' não existe nesse dicionário. \n")
