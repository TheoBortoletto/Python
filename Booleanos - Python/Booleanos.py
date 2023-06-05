print("\t - Booleanos: \n")

# Booleanos representam dois valores: 'True' ou 'False'

print(" - Exemplo de expressão booleana, checar se é veredadeiro ou falso com um 'if': \n")

a = 200
b = 199

if b > a:
    print(b, "é maior do que", a)

else:
    print(a, "é maior que", b, "\n")

### 

print(" - Avaliar valores e variáveis, retornando True ou Flase: \n")

print(bool("Hello"))
print(bool(0), "\n")

txt = "Hello"
txt2 = ""

print(bool(txt))
print(bool(txt2), "\n")

###

print(" - A maioria dos valores são verdadeiros: \n")

print(bool("abc"))
print(bool(123))
print(bool(["apple", "pear", "orange"]), "\n")

### 

print(" - Alguns valores são falsos: \n")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}), "\n")

### 

print(" - Objetos que retornam 0, também é avaliado como 'False': \n")

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj), "\n")

### 

print(" - Funções podem retornar um booleano: \n")

def myFunction() :
  return True

print(myFunction(), "\n")

### 

# Você pode executar o código com base na resposta booleana de uma função:

print(" - Imprimir 'SIM!' se a função retornar True, caso contrário imprima 'NÃO!': \n")

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
