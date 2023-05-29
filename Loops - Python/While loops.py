### Loops do Python ###

### While loop ###

print("\t --- While loop: --- \n")

i = 1
while i < 6: # Enquanto essa condição for verdadeira
  print(i)   # Imprima o vaor de i (note que imprimirá só até o numero 5)
  i += 1     # Incremento


### A declaração 'break' ###
### Com a instrução 'break' podemos parar o loop mesmo se a condição while for verdadeira ###

print("\t --- A declaração'break': --- \n")

j = 1
while j < 6:   # Enquanto essa condição for verdadeira
  print(j)     # Imprima o valor de j
  if (j == 3): # Se j for igual a 3 o loop para
    break
  j += 1       # Enquanto j não for igual a 3, incrementa


### A declaração 'continue' ###
### com a instrução 'continue', podemos interromper a iteração atual e continuar com a próxima ###

print("\t --- A declaração 'continue': --- \n")

k = 0
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)


### A declaração 'else' ###

print("\t --- Declaração 'else': --- \n")

l = 1 
while l < 6:
  print(l)
  l += 1
else:
  print(l, "não é mais, menor que 6 \n")