class Animal:
  def eat(self):
    print("The animal is eating.")
class Dog(Animal):
  def bark(self):
    print("The dog is barking.")
dog1 = Dog()
dog1.eat()
dog1.bark()

class Person:
  def __init__(self, name):
    self.name = name
class Student(Person):
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

#Level 1: Base Parent Class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
#Level 2: Child of Person and Parent of Manager
class Employee(Person):
  def __init__(self, name, age, job_title, salary):
    super().__init__(name, age)
    self.job_title = job_title
    self.salary = salary
#Level 3: Subclass of Employee
class Manager(Employee):
  def __init__(self, name, age, job_title, salary, department):
    super().__init__(name, age, job_title, salary)
    self.department = department
#Testing the classes
manager = Manager("Alice", 35, "Project Manager", 80000, "IT Unit")
print(f"{manager.name} is a {manager.job_title} with monthly salary of Php{manager.salary:.2f}")



#Level 1: Base parent class
class Animal:
  def __init__(self, kingdom = "Animalia"):
    self.kingdom = kingdom
  def eat(self):
    print("Consuming food for energy.")
#Level 2: Child of Animal and Parent of Dog
class Mammal(Animal):
  def __init__(self, kingdom, warm_blooded: True):
    super().__init__(kingdom) #passes kingdom up to Animal constructor
    self.warm_blooded = warm_blooded
  def nurse_young(self):
    print("Feeding milk to offspring.")
#Level 3: Sub class of Mammal
class Dog(Mammal):
  def __init__(self, kingdom, warm_blooded, breed, name):
    super().__init__(kingdom, warm_blooded) #Ask Mammal to handle kingdom and warm_blooded initialization
    self.breed = breed
    self.name = name
  def bark(self):
    print(f"{self.name} the {self.breed} says Woof!")

#Testing the Multi-level Biology Chain
my_dog = Dog("Animalia", True, "Shih Tzu", "Bruno")
#Accessing the attributes inherited from 3 levels
print("Kingdom: ", my_dog.kingdom)
#print(f"Kingdom: {my_dog.kingdom})
print("Warm-blooded: ", my_dog.warm_blooded)
print("Breed: ", my_dog.breed)
#Executing methods inherited from all 3 levels
my_dog.eat()
my_dog.nurse_young()
my_dog.bark()