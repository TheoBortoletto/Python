print("\t - Números do Python: \n")

# Existem 3 tipos numéricos no Python: int, floaat, complex

print("Exemplos: \n")

x = 10 # int
y = 15.55 # float
z = 5j # complex

print(x, "= int \n")
print(y, "= float \n")
print(z, "= complex \n")

### 

print(" - Verificar o tipo de dado numérico, utilize a função 'type()': \n")

print(type(x))
print(type(y))
print(type(z), "\n")

###

print(" - Conversão de tipos numéricos: \n")

num1 = 1    # int
num2 = 2.8  # float
num3 = 1j   # complex

#convert from int to float:
a = float(num1)

#convert from float to int:
b = int(num2)

#convert from int to complex:
c = complex(num3)

print(a)
print(b)
print(c, "\n")

print(type(a))
print(type(b))
print(type(c), "\n")

# Não é possível converter números complexos em outro tipo de número

###

print("\t - Número aleaatório: \n")

# É preciso importar o módulo 'random' para que o Python gere números aleatórios

import random # Importando módulo

print(" - Imprimindo um número aleatório: \n")

print(random.randrange(1,100), "\n")
