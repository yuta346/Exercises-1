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
        if type(other)==int:
            return Vector3D(self.x*other, self.y*other, self.z*other)
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __rmul__(self,other):
       if type(other)==int:
            return Vector3D(self.x*other, self.y*other, self.z*other)
       return self.x*other.x+ self.y*other.y + self.z*other.z

    def __eq__(self,other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __sub__(self,other):
        return Vector3D(self.x - other.x, self.y - other.y,self.z - other.z)
    
def sort_vectors(vect_lst):
    result = []
    for vect in vect_lst:
        abs_val = abs(vect)
        result.append((vect,abs_val),)
    result.sort(key=lambda x: x[1])
    return [vect[0] for vect in result]

vec1 = Vector3D(1, 2, 3)
vec2 = Vector3D(y=1, z=3)
vec3 = Vector3D()
vect_lst = [vec1, vec2, vec3]
# print(sort_vectors(vect_lst))
# print(vec1 *3)  #== Vector3D(3, 15, 9)
# print(3*vec3)
rvec1 = vec1 * 3
rvec2 = vec2 * 2
lvec1 = 3 * vec1
# print(rvec1)
# print(rvec2)
# print(lvec1)
print(vec1 * vec2) 
print(vec1 * vec3) 
print(vec1 * vec1) 


# vec1 = Vector3D(1, 5, 3)
# vec2 = Vector3D(4, 4, 1)
# vec3 = Vector3D(1, 5, 2)
# print(vec1*vec2) #== 18

# print(vec1 < vec2) #== False
# print(vec3 < vec1) #== True
# print(vec1 > vec2) #== True
# print(vec1 > vec3) #== False