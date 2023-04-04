########################## 1 #################################
# class Rectangle:

# 	def __init__(self, sideA=0, sideB=0):
# 		self.sideA = sideA
# 		self.sideB = sideB

# 	def getArea(self):
# 		return self.sideA * self.sideB
  
# 	def getPerimeter(self):
# 		return 2 * (self.sideA + self.sideB)

# class Circle:
#     pi = 3.141592
#     def __init__(self, radius):
#         self.radius = radius

#     def getArea(self):
#         return round(Circle.pi*self.radius*self.radius)

#     def getPerimeter(self):
#         return round(2*Circle.pi*self.radius)
################################# 2 #################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def compare_age(self, other):
    if other.age < self.age:
      s = 'younger than'
    elif other.age > self.age:
      s = 'older than'
    elif other.age == self.age:
      s = 'the same age as'
    return '{} is {} me.'.format(other.name,s)

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)