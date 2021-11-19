list1=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for num in list1:
	if num%2==0:
		even=even+1
	else:
		odd=odd+1
print("Even number in list:",even)
print("Odd number in list:",odd)
