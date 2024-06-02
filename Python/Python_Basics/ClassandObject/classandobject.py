#now lets try defining class and object in same python file

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("ballaladeva", 66)

print(p1.name)
print(p1.age)