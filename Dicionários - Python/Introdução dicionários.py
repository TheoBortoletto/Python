### Dicionário ###

### Os dicionários são usados para armazenar valores de dados em pares chave:valor. ###

### Um dicionário é uma coleção que é ordenada*, modificável e não permite duplicatas. ###

### Criar dicionário ###

print("\t Criando um dicionário: \n")

carsDict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

print(carsDict, "\n")

### Imprimindo o valor de uma chave ###

print("\t Imprimindo o valor de uma chave: \n")

theoDict = {
  "altura": 1.90,
  "idade": 19,
  "nacionalidade": "Brasileiro"
}

print(theoDict["idade"], "\n")

### Dicionários são ordenadods, são mutáveis (podemos alterar, adicionar ou remover itens após a criação de um dicionário) ###

### Não permitem duplicatas ###

print("\t Não permitem duplicatas: \n")


teslaDict = {
  "marca": "Tesla",
  "modelo": "Model X",
  "ano": 2019,
  "ano": 2020  # Note que '2020' será imprimido
}

print(teslaDict, "\n")

### Tamanho do dicionário ###

print("\t Tamanho do dicionário: \n")

print(len(teslaDict), "É o tamanho do 'teslaDict'. \n")

### Itens do Dicionário - Tipos de Dados ###

print("\t Itens do Dicionário - Tipos de Dados: \n")

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict, "\n")

### Da perspectiva do Python, os dicionários são definidos como objetos com o tipo de dados 'dict' ###

print("Dicionários são tipos de dados:",type(thisdict), "\n")

### Construtor de Dicionários - dict() ###

print("\t Construtor de dicionários - 'dict()': \n")

JohnDict = dict(name = "John", age = 36, country = "Norway")
print(JohnDict)