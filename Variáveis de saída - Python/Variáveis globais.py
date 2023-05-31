


print(" - Variáveis globais: \n")

# Variáveis ​​criadas fora de uma função são conhecidas como variáveis ​​globais.

# As variáveis ​​globais podem ser usadas por todos, tanto dentro quanto fora das funções.

print(" - Criando uma variável fora de uma função e usando-a dentro desta função: \n ")

a = "20 anos"

def printIdade():
    print("O Théo tem " + a)
    print("\n")

printIdade()

###

# Se você criar uma variável com o mesmo nome dentro de uma função, esta variável será local, 
# e só poderá ser utilizada dentro da função. A variável global com o mesmo nome permanecerá 
# como estava, global e com o valor original.

###


print(" - Criando uma variável dentro de uma função commo mesmo nome da varíavel global (que esta fora da função): \n")

company = "Valdac"

def printCompany():
    company = "Apple"
    print("Eu trabalho na", company)
    print("\n")

printCompany()

print("Eu trabalho na", company, "\n")

###

print(" - A palara chave 'global': \n")

# Se usarmos a palavra chave 'gllobal', a variável pertennce ao escopo global

def globalFunc():
    global x
    x = "fantastic"

globalFunc()

print("Python is " + x + "\n")

print("Alterando o valor de uma variável global dentro de uma função: \n")

college = "ESPM"

def printCollege():
    global college
    college = "Senac"

printCollege()


print("Eu estudo no " + college + '\n')

