# Matemática do Python

print("\t - Matemática do Python: \n")

print(" - Funções 'min()' e 'max()': \n")

# As funções min() e max() podem ser usadas para encontrar o valor mais baixo ou mais alto em um iterável

numMin = min(5, 10, 25)
numMax = max(5, 10, 25)

print("O número mínimo é:", numMin)
print("O número máximo é:", numMax, "\n")

###

print(" - Função 'abs()': \n")

# A abs()função retorna o valor absoluto (positivo) do número especificado:

x = abs(-657)

print("Número absoluto:", x, "\n")

###

print(" - Função 'pow()' - Potência: \n")

potencia = pow(4, 3)

print("Resultado da potência:", potencia, "\n")

### 

print("\t - O múlodo de matemática: \n")

print(" - Alguns exemplos das referências que podemos usar com o modulo 'math': \n")

import math  # Esse módulo estende a lista de funções matemáticas

###

print("- Raiz quadrada: \n")

raiz = math.sqrt(64)
print("Raiz quadrada de 64 é:", raiz, "\n")

###

print("- Métodos de arredondamento: \n")

num1 = math.ceil(1.4)   # Arredonda um número para cima até o inteiro mais próximo
num2 = math.floor(1.4)  # arredonda um número para baixo até o inteiro mais próximo 

print("Número arredondado pra cima:", num1)
print("Número arredondado pra baixo:", num2, "\n")

###

print("- Retornar o valor de PI: \n")

pi = math.pi

print("O número PI é igual a:", pi, "\n")

###

# Link da refêrencia completa do módulo de matemática: 
# https://www.w3schools.com/python/module_math.asp