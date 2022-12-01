# class Cylinder:
# 	pi=3.14
# 	def __init__(self,height=1,radius=1):
# 		self.height=height
# 		self.radius=radius

# 	def volume(self):
# 		return (Cylinder.pi*(self.radius**2)*self.height)

# 	def surface_area(self):
# 		a=((2*Cylinder.pi*self.radius)*(self.height+self.radius))
# 		return a

# c=Cylinder(2,3)
# print(c.volume())
# print(c.surface_area())

# class Line():
# 	def __init__(self,coor1,coor2):
# 		self.coor1=coor1
# 		self.coor2=coor2
# 	def distane(self):
# 		x1,y1=self.coor1
# 		x2,y2=self.coor2
# 		return ((x2-x1)**2 + (y2-y1)**2)**0.5

# 	def slope(self):
# 		x1,y1=self.coor1
# 		x2,y2=self.coor2

# 		return (y2-y1)/(x2-x1)
# coor1=(3,2)
# coor2=(8,10)

# a=Line(coor1,coor2)
# print(a.distane())
# print(a.slope())

class Account():

	def __init__(self,name,AccountBalance=0):
		self.name=name
		self.AccountBalance=AccountBalance
	def __str__(self):
		return "Account owner: {} \n Balance : {}".format(self.name,self.AccountBalance)
	def balance(self):
		return self.AccountBalance
	def deposit(self,amount):
		self.AccountBalance+=amount
		return "Deposite Accepted"
	def withdrawal(self,amount):
		if self.AccountBalance >= amount:
			self.AccountBalance-=amount
			return "withdrawal Accepted"
		else:
			return "Funds Unavailable!"
acc=Account("jose",100)

print(acc)
print(acc.balance())
print(acc.deposit(50))
print(acc.balance())
print(acc.withdrawal(50))
print(acc.balance())
print(acc.withdrawal(150))