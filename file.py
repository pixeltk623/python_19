# file = open("demo.txt", 'r')

# # print(file.read())

# # print(file.read(10))

# # print(file.readlines())


# file = open("test.txt", "w")

# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")

# file.close()



# file = open("test.txt", "r")

# print(file.read())

# #print(file)

# file = open('test12.txt','a')
# file.write("This will add this line")
# file.close()

# with open("test12.txt") as file:
# 	data = file.read()

# 	print(data)


# with open("test12.txt", "r") as file:
# 	data = file.readlines()

# 	for line in data:
# 		word = line.split()
# 		print (word)


# file1 = open("test12.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# file1.writelines(L)
# file1.close()


# file1 = open("test12.txt", "a") # append mode
# file1.write("Today \n")
# file1.write("Today \n")
# file1.close()


# file1 = open("test12.txt", "w") # write mode
# file1.write("Tomorrow \n")
# file1.close()



# file1 = open("test12.txt", "r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()

