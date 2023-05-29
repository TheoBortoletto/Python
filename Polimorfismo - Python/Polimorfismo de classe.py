# Polimorfismo de Classe # 

# O polimorfismo é frequentemente usado em métodos de classe, onde podemos ter várias classes com o mesmo nome de método. #

print("Polimorfismo de classe \n")


# Por exemplo, digamos que temos três classes: Carro, Barco, e Aeronave, e todas elas têm um método chamado mover(): #

class Carro:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def mover(self):
    print("Dirija!")

class Barco:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def mover(self):
    print ("Conduza!")

class Aeronave:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def mover(self):
    print("Vôe!")

carro1 = Carro("Ford","Mustang")
barco1 = Barco("Ibiza", "Touring 20")
aeronave1 = Aeronave("Boeing", "747")

for x in (carro1, barco1, aeronave1):
  x.mover()
  print("\n")

# Polimorfismo de Classe e Herança #

print("Polimorfismo de classe e herança: \n")


# Se usarmos o exemplo acima e criarmos uma classe pai chamada Vehicle, e criarmos Car, Boat, Plane classes filhas de Vehicle, as classes filhas herdarão os Vehiclemétodos, mas poderão sobrescrevê-los:

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  print(x.brand, x.model)
  # print(x.model)
  x.move()
  print("\n")

# As classes filhas herdam as propriedades e métodos da classe pai.

# No exemplo acima você pode ver que a Carclasse i está vazia, mas ela herda brand, modele move()de Vehicle.

# As classes Boate Planetambém herdam brand, modele move()de Vehicle, mas ambas substituem o move()método.

# Por causa do polimorfismo, podemos executar o mesmo método para todas as classes.