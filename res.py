import re

# pattern = '^a...s$'

# myNewString = "aumas"

# result = re.match(pattern, myNewString)

# if result:
# 	print("Got")
# else:
# 	print("Not Found")


# string = 'hello 12 hi 89. Howdy 34'
# pattern = '\d+'

# result = re.findall(pattern, string) 
# print(result)

# string = 'Twelve:12 Eighty nine:89 Fifty six:56.'
# pattern = '\d+'

# result = re.split(pattern, string) 
# print(result)




#print(result)

# test_string = 'ahars'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")


# string = 'Twelve:12 Eighty nine:89 Nine:9.'
# pattern = '\d+'

# # maxsplit = 1
# # split only at the first occurrence
# result = re.split(pattern, string, 1) 
# print(result)


# string = 'abc 12\
# de 23 \n f45 6'

# # matches all whitespace characters
# pattern = '\s+'

# # empty string
# replace = 'Krishna'

# new_string = re.sub(pattern, replace, string) 
# print(new_string)

# string = 'abc 12\
# de 23 \n f45 6'

# # matches all whitespace characters
# pattern = '\s+'
# replace = ''

# new_string = re.sub(r'\s+', replace, string, 1) 
# print(new_string)


# string = 'abc 12\
# de 23 \n f45 6 This is Kumar'

# # matches all whitespace characters
# pattern = '\s+'

# # empty string
# replace = ''

# new_string = re.subn(pattern, replace, string) 
# print(new_string)


import json

# x =  '{ "name":"John", "age":30, "city":"New York"}'

# y = json.loads(x)

# print(y)

# print(y['name'])


# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # print(x['age'])

# # exit()
# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)


#print(json.dumps({"name": "John", "age": 30}))
#print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
#print(json.dumps(None))


# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }


# print(x['name'])

# print(json.dumps(x))


# print(json.dumps(x, indent=4))

# print(json.dumps(x, indent=4, sort_keys=True))

import re
# if re.match("f.o","fooooo"):
#     print("Matched")
# else:
#     print("Not matched")


# if re.match("f.o$","frso"):
#     print("Matched")
# else:
#     print("Not matched")


# if re.match("..$","fo"):
#     print("Matched")
# else:
#     print("Not matched")


import re
number = input()
if re.match("[1-9][0-9][a-zA-Z]{3}[0-9]{4}$",number):
    print('valid')
else:
    print('invalid')



