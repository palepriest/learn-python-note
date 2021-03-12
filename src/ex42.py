# -*- coding:utf-8 -*-

## animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name
    
## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## person has a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic
        super(Employee, self).__init__(name)
        ## ?? employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(oject):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet named of satan
mary.pet = satan

## frank is-a employee, who has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet named of rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a instance of Salmon, which is-a fish
crouse = Salmon()

## crouse is-a instance of Salmon, which is-a fish
harry = Halibut()


