### Funções ###

### Uma função só é executada quando é chamada ###

### Criar Função ###

print("\t --- Criando uma função e a execuntando: --- \n")

def hello(): # Criando a função
  print("Hello, world!!!") 

hello() # Executando a função
print("\n")

### Definindo argumentos em uma função ###

print("\t --- Definindo argumentos de uma função e a execuntando: --- \n")

def firstName(fname):
  print(fname + " Bortoletto")

firstName("Théo")
firstName("Fernando")
firstName("Fred")
print("\n")

### Do ponto de vista de uma função: ###
### Um PARÂMETRO é a variável listada entre parênteses na definição da função. ###
### Um ARGUMENTO é o valor que é enviado para a função quando ela é chamada. ###

print("\t --- Função com mais de um argumento: --- \n")

def fullName(fname, lname):
  print(fname + " " + lname) # Concatenando string

# Uma função que espera 2 argumentos sempre deve receber 2 argumentos #

fullName("Théo","Bortoletto")
fullName("Alan", "Nazareth")
fullName("Beatriz", "Bela")
fullName("Larissa", "Di Roberto")
fullName("Lívia", "Mazur")
print("\n")

### Argumentos arbitrários (*args) ###

print("\t --- Argumentos arbitrários: --- \n")

### Se não souber quantos argumentos serão passados na função, adicine um '*' antes do nome do parâmetro da função na definição da função ###

def kidsName(*kids):
  print("A criança mais nova é " + kids[1])

kidsName("Gabriela", "Ryan", "Julia")
print("\n")

### Argumentos de palavra-chave ###

print("\t --- Argumentos palavras-chave: --- \n")

### É possível enviar argumentos com a sintaxe: 'chave = valor'. Desta forma, a ordem dos argumentos não importa ###

def kids(child3, child2, child1):
  print("A criança mais velha é " + child2)

kids(child1 = "Julia", child2 = "Gabriela", child3 = "Ryan")
print("\n")

### Argumentos arbitrários de palavra-chave (**kwargs) ###

### Se você não souber quantos argumentos de palavra-chave serão passados para sua função, adicione dois asteriscos: ''**' antes do nome do parâmetro na definição da função. ###

print("\t --- Argumentos arbitrários de palavra-chave: --- \n")

def name(**name):
  print("O primeiro nome dele é " + name["FirstName"])

name(FirstName = "Alan", LastName = "Nazareth")
print("\n")

### Valor do parâmetro padrão ###

### Se chamarmos uma função sem argumento, ela usará o valor padrão ###

print("\t --- Valor do parâmetro padrão de uma função: --- \n")

def country(country = "na Austrália"):
  print("Eu moro " + country)

country("na Suíça")
country("na Índia")
country() # Retornará Austrália
country("no Brasil")
print("\n")

### Passando uma lista como argumento ###

print("\t --- Passando uma lista como um argumento: --- \n")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
print("\n")

### Valores de retorno ###

### Para permitir que uma função retorne um valor, use o return ###

print("\t --- Valores de retorno: --- \n")

def mult(a):
  return 5 * a

print(mult(5))
print(mult(6))
print(mult(7))
print("\n")

### Declaração 'pass' ###

### Funções não podem estar vazias, mas se por algum motivo houver uma função sem centeúdo, coloque 'pass' abaixo pra evitar erros ###

def myfunction2():
  pass

#





