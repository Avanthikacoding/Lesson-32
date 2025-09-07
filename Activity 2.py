"""Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog."""
from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class lion(animal):
    def move(self):
        print("The lion can jump in the air")

class human(animal):
    def move(self):
        print("A human can walk")
class cat(animal):
    def move(self):
        print("The cat can run")
l1 = lion()
l2 = human()
l3 = cat()
l1.move()
l2.move()
l3.move()
