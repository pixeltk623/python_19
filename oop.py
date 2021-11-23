# class MyClass:
# 	x = 5

# objectOClass = MyClass()

# #print(objectOClass)

# print(objectOClass.x)
	

# class Person:
# 	def __init__(self,name,email,mobile):
# 		self.name = name;
# 		self.email = email;
# 		self.mobile = mobile;

# 	def getMyFullname(self):
# 		print("Hello This is "+self.name+" kumar")

# objectOClass = Person("Sanjeev", "s@gmail.com", 9835401515)

# # del objectOClass


# objectOClass.name = "Raushan"
	
# # print(objectOClass.name)
# # print(objectOClass.email)
# # print(objectOClass.mobile)

# objectOClass.getMyFullname()


class Manager:
	def __init__(self, fname, email):
		self.fname = fname
		self.email = email

	def printManagerName(self):
		print(self.fname, self.email)

class Employee(Manager):
	def __init__(self, fname, email):
		Manager.__init__(self,fname,email)

	def getMyAddress(self):
		return "Gotri"

objectOClass = Employee("Sanjeev", "s@gmail.com")

objectOClass.printManagerName()
print(objectOClass.getMyAddress())