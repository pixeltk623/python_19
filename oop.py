# # class MyClass:
# # 	x = 5

# # objectOClass = MyClass()

# # #print(objectOClass)

# # print(objectOClass.x)
	

# # class Person:
# # 	def __init__(self,name,email,mobile):
# # 		self.name = name;
# # 		self.email = email;
# # 		self.mobile = mobile;

# # 	def getMyFullname(self):
# # 		print("Hello This is "+self.name+" kumar")

# # objectOClass = Person("Sanjeev", "s@gmail.com", 9835401515)

# # # del objectOClass


# # objectOClass.name = "Raushan"
	
# # # print(objectOClass.name)
# # # print(objectOClass.email)
# # # print(objectOClass.mobile)

# # objectOClass.getMyFullname()


# # class Manager:
# # 	def __init__(self, fname, email):
# # 		self.fname = fname
# # 		self.email = email

# # 	def printManagerName(self):
# # 		print(self.fname, self.email)

# # class Employee(Manager):
# # 	def __init__(self, fname, email):
# # 		Manager.__init__(self,fname,email)

# # 	def getMyAddress(self):
# # 		return "Gotri"

# # objectOClass = Employee("Sanjeev", "s@gmail.com")

# # objectOClass.printManagerName()
# # print(objectOClass.getMyAddress())

# # class ClassName(object):
# # 	"""docstring for ClassName"""
# # 	def __init__(self, arg):
# # 		super(ClassName, self).__init__()
# # 		self.arg = arg

# class Company():
	
# 	def __init__(self, name, email, mobile):
# 		self.name = name
# 		self.email = email
# 		self.mobile = mobile

# 	def getName(self):
# 		print(self.name)

# class Employee(Company):
# 	__newSalary=54564
# 	def __init__(self, name, email, mobile):
# 		Company.__init__(self,name,email,mobile)
# 		self._salary = "5456465"

# 	def getMobileNumber(self):
# 		print(self.mobile)

# 	def getSalary(self):
# 		print(self._salary)
# 		# super(ClassName, self).__init__()
# 		# self.arg = arg

# 	def getNewSalary(self):
# 		print(self.__newSalary)
		

# # objectT = Company("Sharvan", "s@gmail.com","5465465")

# # print(objectT)

# # objectT.getName()

# objectT = Employee("Sharvan", "s@gmail.com","5465465")
# # print(objectT)
# # objectT.getName()
# # objectT.getMobileNumber()


# # objectT.getSalary()

# # print(objectT.__newSalary)

# objectT.getNewSalary()


# class A():
# 	def __init__(self,name):
# 		self.name = name;

# class B(A):
# 	def __init__(self, name):
# 		super(A, self).__init__()
# 		self.name = name

# 	def getName(self):
# 		print(self.name)

# objectT = B("Kumar")

# # print(objectT)

# objectT.getName()


# class A():
# 	def __init__(self, name='Kumar'):
# 		self.name = name

# 	def __str__(self):
# 		return self.name

# objectT = A()
# objectT2 = A("Sharvan")
# objectT3 = A("Krishna")
# objectT4 = A()

# print(objectT)
# print(objectT2)
# print(objectT3)
# print(objectT4)
		

# myTupe = ("Sharvan","Rahul","Kumar")

# print(myTupe)

# newvar = iter(myTupe)

# print(next(newvar))
# print(next(newvar))
# print(next(newvar))
# print(next(newvar))

# myTupe = "Sharvan"

# print(myTupe)

# newvar = iter(myTupe)

# print(next(newvar))
# print(next(newvar))
# print(next(newvar))
# print(next(newvar))

class MyNumbers:
	def __iter__(self):
		self.a = 1

		return self;

	def __next__(self):
		x = self.a
		self.a += 1
		return x

myclass = MyNumbers()

myIter = iter(myclass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))