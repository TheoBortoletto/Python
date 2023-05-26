### Criar tupla ###

print("\t Tuplas: \n")

fruitTuple = ("Maçã", "Banana", "Cereja")
print(fruitTuple)
print("\n")


### Tuplas permitem itens com o mesmo valor ###
print("\t Tupla com itens com o mesmo valor: \n")

sameValueTuple = ("Orégano", "Tomate", "Arroz", "Orégano", "Feijão")
print(sameValueTuple)
print("\n")

### Comprimento da tupla: para determinar quantos itens uma tupla tem, usa-se a função len() ###
print("\t Tupla exemplo para mostrar a quantidade de itens dentro dela: \n")

animalsTuple = ("Gato", "Cachorro", "Jaguatirica", "Ornintorrinco")
print(animalsTuple)
print("Quantidade de itens da tupla acima:", len(animalsTuple)) 
print("\n")

### Criar tupla com apenas um item ###
print("\t tupla com apenas um item: \n")

oneItemTuple = ("Teste de Tupla",) # É necessário uma vírgula para o Python reconhecer que é ima                                      tupla de um item
print(oneItemTuple)
print("O tipo de dado acima é:", type(oneItemTuple))
print("\n")

### Itens de Tupla - Tipos de Dados ###
print("\t Itens de tupla podem ser qualuer tipo de dados: \n")

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1, "- String - \n")
print(tuple2, "- Int - \n")
print(tuple3, "- Booleano -\n")

print("\t Uma tupla pode conter vários tipos de dados: \n")

dataTuple = ("abc", 23, True, 40, "hello world \n")
print(dataTuple, "\n")

### Construtor Tupla ###

print("\t É possível utilizar o construtor tuple() pr criar uma tupla: \n")

constTuple = tuple(("Olá", "mundo", "!!!")) # Note o duplo parentêses
print(constTuple)
