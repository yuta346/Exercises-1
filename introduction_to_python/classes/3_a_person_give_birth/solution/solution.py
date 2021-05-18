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

    def give_birth(self,name):
        if name:
            baby = Child(name,0,None,[],[self])
            self.children.append(baby)
            if self.spouse:
                self.spouse.children.append(baby)
                baby.parents.append(self.spouse)


class Child(Person):

    def __init__(self,name,age,spouse=None,children=None,parents=[]):
        Person.__init__(self,name,age,spouse,children)
        self.parents = parents

    def get_siblings(self):
        child_list = list()
        for parent in self.parents:
           child_list = list((set(child_list) | set(parent.children)))
        child_list.sort(key=attrgetter('age'))
        return [sibling.name for sibling in child_list if sibling is not self]
