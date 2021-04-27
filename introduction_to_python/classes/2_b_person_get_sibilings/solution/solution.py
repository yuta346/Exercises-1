# # Problem Description
# Using your `Person` class and `Child` class you defined in a previous question, 
# define a method inside the child class, `get_siblings`, that returns a list of names of all the siblings 
# of the child object sorted in increasing order by age.
# Hint: Note that a child can have a half sibling which is a child of one parent but not the other.
#  ## Example
#  ```
#  Jonny = Person("Jonny", 32, Beth, [Max, Annie, Ron])
#  Beth = Person("Beth", 28, Jonny, [Max, Annie, Ron])
#  Max = Child("Max", 5, None, [], [Beth, Jonny])
#  Annie = Child("Annie", 10, None, [], [Beth, Jonny])
#  Ron = Child("Ron", 7, None, [], [Beth, Jonny])
#  Max.get_siblings() == ["Ron", "Annie"]
#  ```
from  operator import attrgetter
class Person:
    def __init__(self,name,age,spouse,children):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

class Child(Person):
    def __init__(self,name,age,spouse,children,parents):
        Person.__init__(self,name,age,spouse,children)
        self.parents = parents
    def get_siblings(self):
        child_set = set()
        for parent in self.parents:
           child_set = list((set(child_set) |set(parent.children)))
        siblings = sorted(child_set,key=attrgetter('age'))
        return [sibling.name for sibling in siblings if sibling is not self]

Jonny = Person("Jonny", 32, None, [])
Beth = Person("Beth", 28, Jonny, [])
Jonny.spouse = Beth
Max = Child("Max", 5, None, [], [Jonny])
Annie = Child("Annie", 10, None, [], [Beth])
Ron = Child("Ron", 7, None, [], [Beth, Jonny])
Jonny.children.extend([Max, Ron])
Beth.children.extend([Annie, Ron]) #Jonny.children U beth.children

Max.get_siblings() == ["Ron", "Annie"]
Ron.get_siblings()
Annie.get_siblings()