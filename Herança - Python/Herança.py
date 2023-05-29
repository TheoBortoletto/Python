 ###############################################################################################

# Cração de classe exemplo que não será usada:

class Person:
  def __init__(person, nome, idade, cidade):
    person.nome = nome
    person.idade = idade
    person.cidade = cidade

  def printP(person):
    print("Me chamo", person.nome, "tenho", person.idade, "anos e moro na cidade de", person.cidade, "\n")

larissa = Person("Larisa Di Roberto", 21, "São Paulo")
larissa.printP()

 ###############################################################################################

### Herança ###

# A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe

print("\t --- HERANÇA: --- \n")
print(" - Classe Pai: (Pessoa) \n")

# Classe PAI: (Pessoa)
# A classe pai pe a classe da qual está sendo herdada, também chamada de classe base

class Pessoa:
  def __init__ (pessoa, pnome, unome):
    pessoa.pnome = pnome
    pessoa.unome = unome

  def printNome(pessoa):
    print(pessoa.pnome, pessoa.unome, "\n")

alan = Pessoa("Alan", "Nazareth")
alan.printNome()

# Classe Filha: (Estudante)

print(" - Classe Filha: (Estudante) \n")

class Estudante(Pessoa):
  pass # Como a classe está apenas herdando, não é necessário colocar método e propriedade                      # Agora a classe 'Estudante' tem as mesmas propriedades e métodos da classe 'Pessoa'

eduarda = Estudante("Eduarda", "Medeiros")
eduarda.printNome()

flavia = Estudante("Flavia", "Sarahim")
flavia.printNome()

carol = Estudante("Carolina", "Gimenez")
carol.printNome()

henrique = Estudante("Henrique", "Marques")
henrique.printNome()

###

# Adicionar a função '__init__()' em uma classe filha

print(" - Adicionar a função '__init__()' em uma classe filha: \n")

# Quando você adiciona a funçao __init__() na classe filha, ela não herdará mais a função '__init__()' do pai
# A função '__init__()' do filho subtitui a do pai 

class Cachorro:
  def __init__(cachorro, nome, raça):
    cachorro.nome = nome
    cachorro.raça = raça

  def printCachorro(cachorro):
    print("Nome do cachorro:", cachorro.nome, "\nRaça do cachorro:", cachorro.raça,"\n")

cachorro1 = Cachorro("Luna", "Vira-lata")
cachorro1.printCachorro()

class Gato(Cachorro):  # Classe Filha
  def __init__(gato, nome, raça):
    Cachorro.__init__(gato, nome, raça)

gato1 = Cachorro("Castiel", "Não tem")
gato1.printCachorro()

# Função 'super()'

# A função 'super()' herdará todos os métodos e propriedades da classe pai

print(" - Função 'super()': \n")

class vgb:
  def __init__(vgb, setor, funcao):
    vgb.setor = setor
    vgb.funcao = funcao

  def printVgb(vgb):
    print("Setor:", vgb.setor, "\nFunção:", vgb.funcao)

class VgbEmp(vgb):
  def __init__(VgbEmp, setor, funcao):
    super().__init__(setor, funcao)

alan = VgbEmp("Moda", "Registrar pedidos")
alan.printVgb()
