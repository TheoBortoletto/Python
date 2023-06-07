### Condições 'if' e 'else' ###

# Python suporta as condições lógicas usuais da matemática:

# Igual a: a == b
# Diferentes: a != b
# Menor que: a < b
# Menor ou igual a: a <= b
# Maior que: a > b
# Maior ou igual a: a >= b

### If e Elif ###

a = 15
b = 10

print("\t -- Condição 'if' e 'elif': -- \n")
print("a = ", a)
print("b = ", b, "\n")


if b < a:
  print(b, "é menor que", a, "\n")
elif a == b:  # elif é a maniera do Python dizer "se as condições anteriores não forem verdadeiras,                     tente esta condição".
  print(b, "é igual a", a, "\n")

### If e Esle ###

num1 = 200
num2 = 33

print("\t -- Condição 'if' e 'else': -- \n")

print("num1 = ", num1)
print("num2 = ", num2, "\n")

if num1 > num2:
  print(num1, "é maior que", num2)
elif num1 == num2:
  print(num1, "é igual a", num2)
else:
  print(num1, "é menor que", num2 )

print("\n")

### If em uma linha ###

num3 = 23
num4 = 24

print("\t -- If em uma linha só: --- \n")

if num3 < num4: print(num3, "é menor que", num3, "\n")

### If e else em uma linha ###

num5 = 233
num6 = 242

print("\t -- If e else em uma linha só: --- \n")

print(num5, "é maior que", num6, "\n") if num5 > num6 else print(num5, "é menor que", num6, "\n")

### Operadores Lógicos ###
### Operador Lógico 'AND' ###

print("\t -- Operador Lógico 'AND': -- \n")

num7 = 200
num8 = 33
num9 = 500

if num7 > num8 and num9 > num7:
  print("Ambas as condições são verdadeiras. \n")

### Operador Lógico 'OR' ###

print("\t -- Operador Lógico 'OR': -- \n")

if num7 > num8 or num7 > num9:
  print("Pelo menos uma das condições é verdadeira. \n")

### Operador Lógico 'NOT' ###

print("\t -- Operador Lógico 'NOT': -- \n")

i = 20
j = 21

if not i > j:
  print(i, "não é maior que", j, "\n")

### If dentro de if ###

print("\t -- If dentro de if: -- \n")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Coloque 'pass' dentro de ifs sem declaração pra evitar erros.