# a = 5

# a = 6
# print(a) # 5
# print(a) # 6


# a variable is a value that can change,
# depending on conditions or on information passed to the program.


# newString = "Test"





# print("t" in newString)

# for x in newString:
# 	print(x)

# print(newString[0])

# print(len(newString))

# for x in xrange(1,10):
# 	pass

# print(newString.lower())

# print(newString.upper())

# a = 5

# if a>2:
# 	print(a)

# a = 8

# if a>12:
# 	print("Hello")
# else:
# 	print("Hi")

# x = input("Enter The First Number: ")
# y = input("Enter The Second Number: ")
# z = input("Enter The Third Number: ")

# if x>=y and x>=z:
# 	print(x, "is greater Number")
# elif y>=x and y>=z:
# 	print(y, "is greater Number")
# else:
# 	print(z, "is greater Number")


# p = int(input("Enter The Principle Amount: "))
# r = int(input("Enter The Rate: "))
# t = int(input("Enter The Time: "))

# ROI = (p*r*t)/100

# totalAmount = p + ROI

# print(ROI)
# print(totalAmount)


# for loop

# while loop

# a loop is a sequence of instruction s
# that is continually repeated until a certain condition is reached.


# for i in range(1,11):
# 	print(i)


# for i in range(1,11):
# 	print("Krishna")


# 1 - 10 

# 5 6 

# i = 1
# while i<=10:
# 	print(i)
# 	# i = i + 4
# 	i += 1


# break

# continue

# for x in range(1,10):
# 	if x==5:
# 		break

# 	print(x)


# for x in range(1,10):
# 	if x==5 or x == 8:
# 		continue

# 	print(x)


# while True:
# 	name = input("Enter Your Name")

# 	if name=='stop':
# 		break


# 	age = int(input("Enter The Age"))

# 	print("Hello", name, " = ", age)



# Python Program to Find the Largest Among Three Numbers
# Python Program to Calculate the Area of a Triangle

# Python Program to Swap Two Variables
# Python Program to Convert Celsius To Fahrenheit
# Python Program to Convert Kilometers to Miles
# Python Program to Check Prime Number
# Python Program to Print all Prime Numbers in an Interval
# Python Program to Find the Factorial of a Number
# Python Program to Display the multiplication Table
# Python Program to Print the Fibonacci sequence
# Python Program to Check Armstrong Number
# Python Program to Find Armstrong Number in an Interval
# Python Program to Find the Sum of Natural Numbers


# userInfo = "My Name is Sharvan kumar"


# print(userInfo)

# print(userInfo[0])

# print(userInfo[5])

# print(userInfo[-1])


# print(userInfo[:4])

# print(userInfo[4:])

# print(userInfo[2:5])

# print(userInfo[-4:-2])

#nameOfUser = "Sharvan Kumar"

# # print(nameOfUser.capitalize())

# # print(nameOfUser.upper())

# # print(nameOfUser.lower())

# print(nameOfUser.replace("Sharvan", "World"))


# firstName = "Sharvan"

# lastName = "Kumar"



# newText = "My first Name is {}" 

# print(newText.format(firstName))


# order = 50

# price = 500

# qty = 5


# text = "My Total order is {qty} and price is {price} and qty is {order}"

# # print(text.format(qty,price,order))


# print(text.format(qty=20,price=500,order=20))


# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

#userInfo = "My Name is Sharvan kumar"

# userInfo="Name"


# print(userInfo)


# print("Name" in userInfo)


# if "Name" in userInfo:
# 	print("Name")
# else:
# 	print("Nahi Hai")


# while True:
# 	name = input("Enter Your Name: ")

# 	if name=='stop':
# 		break


# 	print(name)

# i = 5
# while i<=25:
	
# 	if i==10 or i == 21:
# 		continue

# 	print(i)

# 	i = i + 1


# for x in range(15):
	
# 	if x==5 or x==8:
# 		continue

# 	print(x)


# x = 15
# y = 20
# # print("Before swapping")
# # print(x)
# # print(y)
# # print("After swapping")
# # temp = y
# # y = x
# # x = temp
# # print(x)
# # print(y)

# print("Before swapping")
# print(x)
# print(y)

# x = x + y # 35

# y = x - y # 35 - 20 // 15


# x = x-y # 35 - 15 = 20


# print("After swapping")
# print(x)
# print(y)



# nterms=int(input(""))
# n1,n2=0,1
# count=0
# if nterms<=0:
# 	print("positive Number")
# elif nterms==1:
# 	print("Fibonacci sequence upto",nterms,":")
# 	print(n1)
# else:
# 	print("Fibonacci sequence:")
# 	while count<nterms:
# 		print(n1)
# 		nth=n1+n2
# 		n1=n2
# 		n2=nth
# 		count=count+1


# n=int(input())
# sum=0
# t=n
# while t>0:
# 	d=t%10
# 	sum=(sum+d**3)
# 	t//=10
# if n==sum:
# 	print(n,"is Armstrong Number")
# else:
# 	print(n,"is not Armstrong Number")

# n=int(input(""))
# if n<0:
# 	print("Invalid Number")
# else:
# 	sum=0
# 	while n>0:
# 		sum=sum+n
# 		n=n-1
# 		print("the sum is",sum)

# start=int(input("Start No: - "))
# end=int(input("End Number: - "))

# for i in range(start,end+1):
#     if i>1:
#         for j in range(2,i):
#             if (i%j==0):
#                 break
#             else:
#                 print(i)
                

# n = int(input("Enter The Number: "))

# if n%2!=0:
# 	print("Odd is ", n)
# else:
# 	print("Even")

# sumT = 0
# for x in range(1, 10):
# 	if x%2!=0:
# 		sumT = sumT + x
# print(sumT)


# sumT = 0
# for x in range(1, 10):
# 	if x%2==0:
# 		sumT = sumT + x
# print(sumT)


# n = 10
# fact = 1
# for x in range(1,11):
# 	fact = fact * x
# print(fact)


# for x in range(1,11):
	
# 	if x==8 or x==6 or x==5:
# 		continue

# 	print(x)