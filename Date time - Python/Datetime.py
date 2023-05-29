# Datetime

# Uma data em Python não é um tipo de dado próprio, mas podemos importar um módulo chamado 'datetime' para trabalhar com as datas como objetos de data. 

print("\t - Datetime: \n")

print(" - Importar e imprimir um 'datetime': \n")

import datetime # SERÁ USADO EM TODO ESSE ARQUIVO

x = datetime.datetime.now()
print("Data e horário de agora:",x, "\n") # Vai retornar 3 horas a mais do que o de Braília.

###

print(" - Retornar ano e o dia da semana:\n")

print("Ano atual:", x.year)
print("Dia da semana:", x.strftime("%A \n"))

###

print(" - Criando um objeto data e imprimindo apenas o dia: \n")

# Para criar uma data, podemos usar a classe 'datetime()' (contrutor) do módulo 'datetime'

# A classe 'datetime()' requer três parâametros para criar uma data: ano, mês, dia.

anoDiaMes = datetime.datetime(2023, 5, 23)

print("Data de hoje:", anoDiaMes, "\n")

###

print(" - Método 'strftime()': \n")

# O 'datetime' tem um método para formatar objetos de data em strings legíveis:

# O método é chamad de 'strftime()' e recebe um parâmetro, 'format', para especificar o formato da string retornada.

print(" - Imprimindo o mês: \n")

month = datetime.datetime(2023, 5, 23)

print(month.strftime("Mês de hoje: %B \n"))

# Link da referência dos formatos de 'strftime()':   

# https://www.w3schools.com/python/python_datetime.asp
