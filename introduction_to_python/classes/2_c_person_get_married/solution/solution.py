# # Problem Description
# Using your `Person` class and `Child` class you defined in a previous question, 
# define a method, `get_married`, that consumes `self` and `other` and sets the spouse of both person 
# objects to be the other person.

#  ## Example
#  ```
#  Anton = Person("Anton", 29, None, [])
#  Nell = Person("Nell", 26, None, [])
#  Anton.get_married(Nell) == None
#  Anton.spouse == Nell
#  Nell.spouse == Anton
#  ```
from  operator import attrgetter
class Person:
    def __init__(self,name,age,spouse,children):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children
    def get_married(self,other):
        self.spouse = other
        other.spouse = self

class Child(Person):
    def __init__(self,name,age,spouse,children,parents):
        super().__init__(name,age,spouse,children)
        self.parents = parents
    def get_siblings(self):
        child_set = set()
        for parent in self.parents:
           child_set = list((set(child_set) |set(parent.children)))
        siblings = sorted(child_set,key=attrgetter('age'))
        return [sibling.name for sibling in siblings if sibling is not self]
