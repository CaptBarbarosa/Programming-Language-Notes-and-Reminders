spam = ['cat', 'bat', 'rat', 'elephant']
print("spam[0] is: ",spam[0])
print("spam[-1] is: ",spam[-1])
print("spam[1:3] is: ",spam[1:3])
print("Before deleting with del spam[2], spam is",spam)
del spam[2]
print("After spam is: ",spam)

str_sum = "Hello" + " World"
print(str_sum)

print("Hello "*3)
print([1,2,3,'a']*3)

print(type(int('42')))
print(list('Hello'))

print('theta' in ['alpha','beta','theta','omega'])
print('zeta' in ['alpha','beta','theta','omega'])

cat = ["fat", "orange", "loud"]
size, color, disposition = cat
print("Size:",size," Color: ",color," Disposition: ",disposition)
size, color, disposition = 'skinny', "black", "quiet"
print("Size:",size," Color: ",color," Disposition: ",disposition)


a= 'A'
b= 'B'
print("Before: ",a,b)
a,b = b,a
print("After: ",a,b)


                ###   LIST METHODS    ###

print("\n\n--->Now doing list methods")
numbers = []
numbers.append(1)
print(numbers)

print("---> You can have different data types in list")
mixed_list = [1, 'a', 3.14]
mixed_list.append(True)
mixed_list.append([5, 6, 7])
print(mixed_list)


print("--> You can append a list into another")
list1 = [1,2,3]
list2 = [4,5,6]
list1.append(list2)
print(list1)













