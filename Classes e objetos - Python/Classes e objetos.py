### Classes / Objetos ###

# Criar Classe

print("\t Classe / Objetos: \n\n \t --- Criar Classe: --- \n")

class MyClass: # MyClass = Classe
    x = 5      # x = Propriedade

print(MyClass, "\n")

# Criar Objeto

print("\t --- Criar Objeto: --- \n")

p1 = MyClass()   # p1 = Objeto
print(p1.x, "\n") 

# Função __init__()

# Todas as classes possuem uma função chamada __init__(), que sempre é executada quando a classe está sendo iniciada.

# A função __init__() atribui valores às propriedades do objetos.

print("\t --- Função '__init__()': --- \n")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person = Person("Théo", 20)

print("Nome:", person.name, "\n")
print("Idade:", person.age, "\n")

# Função __str__()

#A função __str__() controla o que deve ser retornado quando o objeto de classe é representado como uma string.

#Se a função __str__() não for definida, a representação de string do objeto é retornada

print("\t --- Função '__str__()': --- \n")

class Quarteirão:
  def __init__(self, avenida, num):
    self.avenida = avenida
    self.num = num

  def __str__(self):
    return f"{self.avenida}({self.num})"
    
avenida1 = Quarteirão("João Martins", 152)

print(avenida1, "\n")

# Métodos do Objeto 
# Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.

print("\t --- Métodos de objeto: --- \n")

class Pessoa:
  def __init__(self, nome, idade):  # Observação: o parâmetro self é uma referência à instância atual da                                             classe é usado para acessar as variáveis pertencentes à classe.
    self.nome = nome
    self.idade = idade

  def myfunc(self):
    print("Olá, meu nome é " + self.nome, "e tenho", self.idade, "anos. \n")

p2 = Pessoa("Théo", 19)
p2.myfunc()

print()

print("\t --- O parâmetro 'Self': --- \n")

# O parâmetro self é uma referência à instância atual da classe e é usado para acessar as variáveis pertencentes à classmethod

# Não é necessário ser nomeado de 'self', você pode chamar como quiser, mas tem que ser o primeirop parâmetro de qualquer função da classe

class Theo:
  def __init__(theo, nome, idade, peso, altura):
    theo.nome = nome
    theo.idade = idade
    theo.peso = peso
    theo.altura = altura

  def theofunc(theo):
    print("Me chamo", theo.nome, "tenho", theo.idade, "anos,", "peso em torno de", theo.peso, "e tenho", theo.altura, "de altura \n")

eu = Theo("Théo", 19, "80kg", "1,90m")
eu.theofunc()

###

print("\t --- Modificar a propriedade de um objeto: -- \n")

class Transporte:
  def __init__(transporte, tipo, ano, marca):
    transporte.tipo = tipo
    transporte.ano = ano
    transporte.marca = marca

  def transportePrint(transporte):
    print("O tipo de transporte é", transporte.tipo, "o ano dele é", transporte.ano, "e marca dele é", transporte.marca, "\n")

onibus = Transporte("Ônibus", 2022, "Volvo")
onibus.transportePrint()

metro = Transporte("Mêtro", "1988", "CPTM")
metro.transportePrint()

metro.ano = 2022  # Propriedade modificada, de 1988 para 2022
metro.transportePrint()

###

print("\t --- Excluir a propriedade de um objeto: -- \n")

class Imovel:
  def __init__(imovel, tipo, metroQuadr, valor):
    imovel.tipo = tipo
    imovel.metroQuadr = metroQuadr
    imovel.valor = valor

  def imovelPrint(imovel):
    print("O tipo do imóvel é", imovel.tipo, "e possui", imovel.metroQuadr, "metros quadrados e no momento vendemos ele por R$", imovel.valor, "\n")

casa = Imovel("casa", "2 mil", "679,000")
casa.imovelPrint()

apartamento = Imovel("apartamento", "86", "500,000")
apartamento.imovelPrint()

del apartamento.tipo     # Propriedade excluida
print(apartamento.tipo)  # Retornará um erro

# É possivel também excluir um objeto -> del casa

# é possível usa a declaração 'pass' caso haja alguma class vazia