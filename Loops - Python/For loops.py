### Loops de For ###

print("\t --- For loop: --- \n")

fruits = ["maçã", "banana", "cereja"]
for x in fruits:
  print(x, "\n")

### Percorrendo uma string ###

print("\t --- Percorrendo um string: --- \n")

for w in "Hello":
  print(w)

### Declaraçãoo 'break' ###

print("\t --- A declaração 'break' em um loop for: --- \n")

cars = ["volvo", "fiat", "honda"]
for i in cars:
  print(i, "\n")
  if i == "fiat":  # Sair do loop quando 'i' for igual a 'fiat'
    break

print("\t --- A declaração 'break' ANTES DO PRINT em um loop for: --- \n")

for i in cars:
  if i == "fiat":  # Sair do loop quando 'i' for igual a 'fiat'
   break
  print(i, "\n")

### A declaração 'continue' ###

print("\t --- A declaração 'continue' em um loop for: --- \n")

names = ["théo", "alan", "beatriz", "larissa", "lívia"]

for j in names:
  if j == "larissa":  # Não irá imprimir 'larissa'
    continue
  print(j)


### Função 'range()' ###

### Para percorrer um conjunto de códigos um número especificado de vezes, podemos usar a função range() ###

### A função range() retorna uma sequência de números, começando em 0 por padrão e incrementando em 1 (por padrão) e termina em um número especificado. ###

print("\t --- Função 'range()': --- \n")

for y in range(10):  # A função começa com 0 por padrão, ou seja, o número 10 não será impresso
  print(y)
print("\n")

### --- ###

print("\t --- Função 'range()' com PARÂMETROS: --- \n")

for h in range(2, 6):  # O número 2 será o valor inicial e 6 será o final mas não será impresso
  print(h)
  
### --- ###

print("\t --- Função 'range()' com parâmetros e INCREMENTO: --- \n")

for t in range(3, 31, 3): # 2: vaor inicial, 30: valor final, 3: incremento 
  print(t)
print("\n")

### --- ###

print("\t --- Else em um loop for: --- \n")

for a in range(6):
  print(a)
else:
  print("\n Loop terminado. \n")

### --- ###

print("\t --- Else com break em um loop for: --- \n")

### O else NÃO será executado se o loop for interrompido por um break ###

for p in range(6):
  if p == 3: break
  print(p)
else:
  print("Loop terminado \n") # Print não será executado

### --- ###

### Loop dentro de loop (loop aninhado) ###

print("\t --- Loop dentro de loop: --- \n")


adj = ["red", "big", "tasty"]
fruit = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruit:
    print(x, y)

### --- ###

### A declaração 'pass' ###

print("\n\t --- Declaração 'pass': --- \n")

### for loops não podem estar vazios, mas se por algum motivo você tiver um for loop sem conteúdo, coloque a declaração pass para evitar erros. ###

for m in [0, 1, 2]:
  pass