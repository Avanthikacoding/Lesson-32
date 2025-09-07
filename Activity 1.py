"""Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example."""
from abc import ABC,abstractmethod
class Myclass(ABC):
    def print(self,x):
        print("Passed value", x)
    @abstractmethod
    def task(self):
        print("I am inside of the parent class")
class Mychildclass(Myclass):
    def task(self):
        print("I am inside of the child class")
c1 = Mychildclass()
c1.task()
c1.print(50)
