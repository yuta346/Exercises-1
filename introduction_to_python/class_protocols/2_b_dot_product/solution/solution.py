#Completed

import math
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
    
    def __lt__(self,other):
        magnitude1 = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        magnitude2 = math.sqrt(other.x**2 + other.y**2 + other.z**2)
        if magnitude1<magnitude2: return True
        return False
    
    def __gt__(self,other):
        magnitude1 = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        magnitude2 = math.sqrt(other.x**2 + other.y**2 + other.z**2)
        if magnitude1 > magnitude2: return True
        return False
    
    def __mul__(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z



vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec3 = Vector3D(1, 5, 2)
print(vec1*vec2) #== 18

# print(vec1 < vec2) #== False
# print(vec3 < vec1) #== True
# print(vec1 > vec2) #== True
# print(vec1 > vec3) #== False