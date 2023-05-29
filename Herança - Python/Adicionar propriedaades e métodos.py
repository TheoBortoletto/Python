# Adicionar Propriedades 

print(" - Adicionar propriedades em Classes: \n")

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printName(self):
    print("Nome:", self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

student1 = Student("Théo", "Bortoletto", 2019)
student1.printName()
print("Ano de graduação:", student1.graduationyear, "\n")

# Adicionar Métodos

print(" - Adicionar Métodos: \n")

class Pessoa:
  def __init__(self, pnome, unome, ano):
    self.primeironome = pnome
    self.ultimonome =  unome

  def printNome(self):
    print(self.primeironome, self.ultimonome)

class Estudante(Pessoa):
  def __init__(self, pnome, unome, ano):
    super().__init__(pnome, unome, ano)
    self.graduacaoano = ano

  def bemvindo(self):
    print("Bem vindo,", self.primeironome, self.ultimonome, "a turma do ano", self.graduacaoano)

estudante1 = Estudante("Théo", "Bortoletto", 2022)
estudante1.bemvindo()