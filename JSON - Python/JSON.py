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






