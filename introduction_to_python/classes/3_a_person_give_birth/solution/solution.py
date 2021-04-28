from  operator import attrgetter
class Person:
    def __init__(self,name,age,spouse=None,children=[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children
    def get_married(self,other):
        self.spouse = other
        other.spouse = self
    def get_divorced(self):
        if self.spouse:
            spouse = self.spouse
            self.spouse = None
            spouse.spouse = None

class Child(Person):
    def __init__(self,name,age,spouse=None,children=None,parents=[]):
        Person.__init__(self,name,age,spouse,children)
        self.parents = parents
    def get_siblings(self):
        child_set = set()
        for parent in self.parents:
           child_set = list((set(child_set) |set(parent.children)))
        siblings = sorted(child_set,key=attrgetter('age'))
        return [sibling.name for sibling in siblings if sibling is not self]
