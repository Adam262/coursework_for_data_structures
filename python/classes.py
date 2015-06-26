class Person:
  type = 'person' # class variable
  favorite_foods = [] # mistaken use of a class variable. would be shared by all instances

  def __init__(self, name):
    self.name = name # instance variable
    self.favorite_foods = [] # correct use of above variable as instance variable

  def add_food(self, food):
    self.favorite_foods.append(food)

  def hello(self):
    print('hello' + self.name)

adam = Person('adam')
adam.hello() #=> 'hello adam'
adam.add_food('pizza')
adam.favorite_foods #=> ['pizza']

# inheiritance
class Coder(Person):
  type = 'coder'

isinstance(adam, Coder) #=> True
isinstance(adam, Person) #=> True
issubclass(Coder, Person) #=> True

