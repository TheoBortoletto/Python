print("\t - Strigs: \n")

# Strings são 'Arrays' (Matrizes)

print(" - Obter um caracter em uma string: \n")

a = "Théo"
print(a[2], "\n")

### 

print(" - Percorrer ma string, utilizando um 'for': \n")

for x in "BANANA":
    print(x)

print("\n")

###

print(" - Obter o comprimento de uma string, utilizanod a função 'len()': \n")

word1 = "Hello world!"
print(len(word1), "\n")

###

print(" - Verificar se uma frase ou caractere está presente em uma string: \n") # Usando o 'in'

txt = "Vivendo o meu melhor momento."

print("momento" in txt, "\n")

###

print(" - Usando 'if' para imprimir strings: \n")

txt2 = "Homem-Aranha"

if "Aranha" in txt2:
    print("Há 'Aranha' na string \n")

### 

print(" - Verificar se em um palavra, não há uma string: \n")

txt3 = "The best things in life are free!"
print("expensive" not in txt, "\n") # Retornará 'True' se for verdadeiro ou 'False" se não

### 

print(" - Usando 'if' para imprimir apenas se uma string não estiver presente: \n")

txt4 = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present. \n")

