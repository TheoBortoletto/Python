print("\t - JSON Python: \n")

### O Python possui um pacote interno chamado json, 
# que pode ser usado para trabalhar com dados JSON.

print(" - Converter JSON pra Python, usando o método 'json.loads()': \n")

import json

# arquivo JSON: 

x = '{"nome": "Théo", "idade": 20, "cidade": "São Paulo"}'

# Convertendo JSON pra Python:

y = json.loads(x)

# O resultado da conversão será um dicionário Python:

print(y["idade"], "\n") 

### 

print(" -  Convertendo Python pra JSON, usando o método 'json.dumps()': \n")

dictionary = {
    "nome": "Eduarda",
    "idade": 21,
    "cidade": "São Paulo"
}

# Convertendo de Pyton para JSON:

convertJson = json.dumps(dictionary)

# O resultato é uma string JSON

print(convertJson, "\n")

#### 

# É possível converter obetos Python dos seguintes tipos em strings JSON: 

### dict
### list
###tuple
### string
### int
### float
### True
### False
### None

### 

print(" - Convertendo objetos Python em strings JSON e imprimindo os valores: \n")

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("\n")

### 

print(" - Convertendo um objeto Python contentdo todos os tipos de dados: \n")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Convertendo para JSON:
y = json.dumps(x)

# O resultado é uma string JSON:
print(y, "\n")

###

#  exemplo acima imprime uma string JSON, mas não é muito fácil de ler, sem recuos e quebras de linha.

# O json.dumps()método possui parâmetros para facilitar a leitura do resultado:

print(" - Usando o parâmetro 'indent' pra definir os números de recuo: \n")

dict = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(dict, indent=4), "\n")

###

print(" - Usando o parâmetro 'sort_keys' para especificar se o resultado deve ser classificado ou não: \n")

person = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(person, indent=4, sort_keys=True), "\n")

