# Iteradores do Python

# Um iterador é um objeto que contém um número cotável de valores, é um objeto que pode ser iteraado, o  que significa que pode percorrer todos os valores


print("\t - Iteradores: - \n")

# Tecnicamente, em Python, um iterador é um objeto que implementa o protocolo do iterador, que consiste nos métodos '__iter__()' e '__next__()'.

# Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis. Eles são contêineres iteráveis dos quais você pode obter um iterador.

print("Retornar o iterador de uma tupla e imprimir cada valor (usando 'iter()' e 'next()'): \n")

fruitsTuple = ("maçã", "banana", "cereja")
myit = iter(fruitsTuple)

print("-", next(myit))
print("-", next(myit))
print("-", next(myit))
print("\n")


# Strings também são iteraveis 

print("Strings também são objetos iteráveis: \n")

string = "BANANA"
myit = iter(string)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit), "\n")

# Criar um Iterador

print("Criando um iterador que retorne números, começando com 1 em sequência: \n")

class Numeros:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

minhaclasse = Numeros()
myiter = iter(minhaclasse)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter), "\n")

# StopIteration

print("Para evitar que uma iteração continue para sempre, podemos usar o 'StopIteration':\n")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)