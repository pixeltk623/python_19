# list1 = ["sharvan","sanjeev","Rahul","sharvan","sanjeev","Rahul","sharvan","sanjeev","Rahul"]

# list2 = [15,78,98,45,78,98,45]
# list3 = [True, False, True, False]
# mixTypeList = ["sharvan","sanjeev",78,98,45,False, True, False,"ABC"]
# list1 = ["sharvan","sanjeev","Rahul"]

# print(list1)
# print(list2)
# print(list3)
# print(mixTypeList)

# print(type(list1))
# print(type(list2))
# print(type(list3))
# print(type(mixTypeList))


# print(len(list1))

# newList = list(("sharvan","sanjeev","Rahul"))

# print(newList)

# print(type(newList))

# print(list1[0])

# print(list1[-1])

# print(list1[3:5])

# print(list1[:3])

# print(list1[3:])

# list1 = ["sharvan","sanjeev","Rahul","sharvan","sanjeev","Rahul","sharvan","sanjeev","Rahul"]

# list2 = [15,78,98,45,78,98,45]
# list3 = [True, False, True, False]
# mixTypeList = ["sharvan","sanjeev",78,98,45,False, True, False,"ABC"]

# print(list1[-4:-2])

# if "Rahul" in list1:
# 	print("Yes")
# else:
# 	print("No")

# list1[0] = "Tops"

# print(list1)

# list1[1:4] = ["Tops", "Tech","Vadodara"]

# print(list1)

# list1.insert(1,"Test")

# print(list1)

# list1.append("Kumar")
# list1.append("Patel")

# print(list1)

# l1 = ["asd","tryrty","poipo"]

# l2 = ["dsd","wryrty","zoipo"]

# t1 = ("asdsa","asd")

# print(l1)
# print(l2)
# #l1.extend(l2)
# l1.extend(t1)

# print(l1)
# print("--Before Remove----")

# print(l1)

# l1.remove("asd")

# print("--After Remove----")

# print(l1)

# l1 = ["asd","tryrty","poipo"]

# l2 = ["dsd","wryrty","zoipo"]

# l1.pop(2)

# print(l1)

# l1.pop()
# l1.pop()
# l1.pop()

# print(l1)

# del l1[0]

# del l1
# print(l1)

# l1.clear()

# print(l1)


# mixTypeList = ["sharvan","sanjeev","Rahul"]

# for x in mixTypeList:
# 	print(x)


# for x in range(len(mixTypeList)):
# 	print(mixTypeList[x])
# 	

# i = 0
# while i<len(mixTypeList):
# 	print(mixTypeList[i])
# 	i = i+1

# [print(x) for x in mixTypeList]

# mixTypeList = ["sharvan","sanjeev","Rahul"]
# newList1 = []

# for x in mixTypeList:
# 	if "R" in x:
# 		newList1.append(x)

# print(newList1)


# newList2 = [x for x in range(10) if x>5]

# print(newList2)

# l1 = ["asd","tryrty","poipo"]


# l11 = [x.upper() for x in l1]

# print(l11)

# A simple program to count pairs with difference k

# def countPairsWithDiffK(arr, n, k):
# 	count = 0
# 	pair = []
# 	for i in range(0, n):
# 		for j in range(i+1, n) :
# 			if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
			
# 				pair.append(arr[i])
# 				pair.append(arr[j])
# 				count += 1		
# 	return {"count":count, "pair":pair}
# arr = [1, 5, 3, 4, 2] #5
# n = len(arr)
# k = 3
# print ("Count of pairs with given diff is ",
# 				countPairsWithDiffK(arr, n, k))



# list1 = ["Tops", "Tech","Vadodara"]

# list1.pop()


# print(list1)


# newList = ["sharvan","rahul","cinmmn","pink"]

# print(newList)

# newList.sort()

# print(newList)


# thisList = [100, 50,26,89,12,36]

# # print(thisList)

# # thisList.sort()

# # print(thisList)


# thisList.sort(reverse=True)

# print(thisList)



# newList = ["Sharvan","rahul","cinmmn","pink"]

# print(newList)

# newList.sort()

# print(newList)


# newList = ["Sharvan","rahul","cinmmn","pink"]

# print(newList)

# newList.sort(key = str.lower)

# print(newList)


# newList = ["sharvan","rahul","cinmmn","pink"]

# print(newList)

# newList.reverse()

# print(newList)

# newList = ["sharvan","rahul","cinmmn","pink"]

# # myList = newList.copy()

# # print(myList)


# myList = list(newList)

# print(myList)


# l1 = ["a","b","c"]
# l2 = [1,2,3]

# l3 = l1 + l2

# print(l3)

# for x in l2:
# 	l1.append(x)


# print(l1)

# l1.extend(l2)

# print(l1)