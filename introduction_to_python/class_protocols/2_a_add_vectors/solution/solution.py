#Completed
class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'(x = {self.x}, y = {self.y}, z = {self.z})'
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3D(x,y,z)

vec1 = Vector3D(1, 2, 3)
vec2 = Vector3D(4, 5, 6)
print(vec1 + vec2)