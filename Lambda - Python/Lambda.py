### Lambda ###

# Sintaxe: 'lambda arguments : expression' #

# Uma função lambda é um pequena função anônima, pode receber qualquer tipo de argumentos mas pode ter apenas uma expressão #

print("\t  Lambda: \n")

print("\t --- Lambda exemplos (subtração): --- \n")

add = lambda a : a + 10
print(add(5)) # a = 5
print("\n")

print("\t --- Lambda exemplos (adição): --- \n")


sub = lambda a, b: a - b # Seta so argumentos que terão valor depois
print(sub(10, 5))        # Valores  de a e b 
print("\n")

print("\t --- Lambda exemplos (multiplicação): --- \n")

mul = lambda i, j: i * j
print(mul(5, 5))
print("\n")

print("\t --- Lambda exemplos (divisão): --- \n")

div = lambda x, y: x / y
print(div(10,2))

