# Escopo do Python 

# Uma variável só está disponível dentro da região em que é criada. Isso é chamado de escopo .

print("\t Escopo do Python: \n")

print("Escopo local: \n")

def func1():
  x = 300
  print(x, "\n")

func1()

print("Função dentro de uma função: \n")

def func2():
  x = 300
  def funcaoDentro():
    print(x)
  funcaoDentro()
  print("\n")

func2()

###

print("Escopo Global: \n")

x = 300

def func3():
  print(x)

func3()

print(x, "\n")

print("Mesma variável mas com valores diferentes: \n")

####

x = 300

def func4():
  x = 200
  print(x)

func4()

print(x, "\n")

###

print("Palavra-chave 'global': \n")
# Se você usar a palavra-chave 'global', a variável pertence ao escopo global

def func5():
  global x
  x = 300

func5()

print(x, "\n")

print("Alterar o valor de uma variável global dentro de uma função: \n")

y = 450

print("Valor da variável no escopo global:", y, "\n")

def myfunc6():
  global y 
  y = 500

myfunc6()

print("Valor alterado da varável globaL:", y, "\n")
