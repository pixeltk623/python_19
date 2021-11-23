# myDict = {
# 	"name" : "Sharvan",
# 	"email" : "s@gmail.com",
# 	"mobile": 9835411515,
# 	"status": True
# }

# print(myDict)
# print(type(myDict))

# print(myDict['name'])
# print(len(myDict))

# x = myDict.get("name")

# print(x)

# x = myDict.keys()

# print(x)

# v = myDict.values()

# print(v)

# print(myDict)

# myDict['address'] = "Vadodara"
# myDict['name'] = "Sanjev"

# print(myDict)

# x = myDict.items()

# print(x)


# if "status" in myDict:
# 	print("yes")


# myDict = {
# 	"name" : "Sharvan",
# 	"email" : "s@gmail.com",
# 	"mobile": 9835411515,
# 	"status": True
# }


# myDict.update({"color":"red"})

# print(myDict)


# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# # double_dict1 = {k:v*2 for (k,v) in dict1.items()}

# # print(double_dict1)

# double_dict1 = {}

# for k,v in dict1.items():
# 	# print(k, v)

# 	double_dict1.update({k:v*2})

# print(double_dict1)

# myDict = {
# 	"name" : "Sharvan",
# 	"email" : "s@gmail.com",
# 	"mobile": 9835411515,
# 	"status": True
# }

# myDict.pop("email")

# print(myDict)


# myDict.remove("email")

# print(myDict)


# myDict.popitem()
# myDict.popitem()
# myDict.popitem()
# myDict.popitem()
# myDict.popitem()

# print(myDict)

# del myDict

# del myDict['status']

# print(myDict)

# myDict.clear()

# print(myDict)


# myDict = {
# 	"name" : "Sharvan",
# 	"email" : "s@gmail.com",
# 	"mobile": 9835411515,
# 	"status": True
# }

# for x in myDict:
# 	print(myDict[x])

# for x in myDict.values():
# 	print(x)


# for x in myDict.keys():
# 	print(x)

# for x,y in myDict.items():
# 	print(x,y)

# d = {'eggs': 3, 'spam': 2, 'ham': 1}

# d2 = {'toast':4,'muffin':5}

# d.update(d2)

# print(d)

# myDict = {
# 	"name" : "Sharvan",
# 	"email" : "s@gmail.com",
# 	"mobile": 9835411515,
# 	"status": True
# }

# newDict = myDict.copy()

# print(newDict)

# newDict = dict(myDict)

# print(newDict)

ourDept = {
	"CSE": {
		"HOD" : "ABC",
		"Location" : "Vadodara"
	} ,
	"IT": {
		"HOD" : "ABC",
		"Location" : "Vadodara"
	}, 
	"EI": {
		"HOD" : "ABC",
		"Location" : "Vadodara"
	} 
}

print(ourDept)