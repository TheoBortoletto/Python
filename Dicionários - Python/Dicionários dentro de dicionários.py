### Criando dicionários 'aninhados' ###

coworkersDict = {
  "alan": {
    "idade": 21,
    "setor": "Moda",
  },
  "beatriz": {
    "idade": 21,
    "setor": "RH"
  }, 
  "lívia" : {
    "idade": 20,
    "setor": "Financias"
  },
  "larissa": {
    "idade": 21, 
  }
}

print("\t Dicionário 'aninhado': \n")

print(coworkersDict, "\n")

### Criar dicionários e adiciona-los em um novo dicionário ###

print("\t Dicionários dentro de um dicionário: \n")

car1 = {
  "modelo": "Mustang",
  "ano": 1970
}

car2 = {
  "modelo": "911",
  "ano": 2020 
}

car3 = {
  "modelo": "Toro",
  "ano": 2019 
}

carsDict = {  # Deixe os nomes iguais pra não dar erro
  "car1": car1,
  "car2": car2,
  "car3": car3
}

print(carsDict, "\n")

### Acessar itens em dicionários aninhados ###

print("\t Acessar itens em dicionários aninhados: \n")

print(carsDict["car1"]["modelo"])