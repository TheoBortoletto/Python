# Variáveis do Python #

print(" - Criando variáveis: \n")

# Uma variável é criada no momento que você atribui valor a ela 

num = 5  # variável int
name = "Théo"  # Variável str

print("Valor da variável 'num':", num)

print("Valor da variável 'name':", name, "\n")

###

print(" - As variáveis podem mudar de valor mesmo depois de declaradas: \n")

x = 10
print("Valor antigo da variável 'x':", x)
x = 20
print("Valor atual da variável 'x'", x, "\n")

###

print(" - É possível especificar o tipo de dados de uma variável, isso pode ser feito com o 'casting': \n")

a = str(3) # = '3'
b = int(3) # = 3
c = float(3) # = 3.0

print(a)
print(b)
print(c, "\n")

print(" - Obter o tipo de uma variável usanod a função 'type': \n")

nome = "Alan"
num2 = 77

print(type(nome))
print(type(num2),"\n")



