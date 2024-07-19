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

print("\n\n---->Now doing list methods append")
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





print("\n\n---->Now doing list methods extend")
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
#numbers.extend(7)
print(numbers)

print("---> Extending a list with a tuple")
fruits = ['apple', 'banana']
fruits.extend(('cherry', 'date'))
print(fruits)

print("---> Extending a list with a string")
letters = ['a', 'b', 'c']
letters.extend('def')
print(letters)

print("---> Extending a list with a dictionary")
keys = [1, 2, 3]
keys.extend({4: 'four','five':5})
print(keys)

print("---> Extending a list within a loop")
combined_list = []
lists_to_add = [[1, 2], [3, 4], [5, 6]]
for lst in lists_to_add:
    combined_list.extend(lst)
print(combined_list)




print("\n\n---->Now doing list methods insert")
# Difference between insert and append is that in insert you can specify the place to insert
print("--->Inserting at 0")
numbers = [1, 2, 3]
numbers.insert(0, 0)
print(numbers)

print("---> Inserting at 1")
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'blueberry')
print(fruits)

print("---> Inserting based on condition")
numbers = [10, 20, 40, 50]
for i, num in enumerate(numbers):
    if num > 30:
        numbers.insert(i,30)
        break

print("---> Inserting a list")
main_list = [1, 2, 3]
main_list.insert(1, [4, 5, 6])
print(main_list)




print("\n\n---->Now doing list methods remove")
print("--->You can remove a given string within a list")
fruits = ['apple', 'banana', 'cherry', 'date']
fruits.remove('banana')
print(fruits)

print("---> You can remove a number")
numbers = [1, 2, 3, 2, 4, 2]
numbers.remove(2)
print(numbers)

print("---> If you want to drop every element within a list:")
colors = ['red', 'green', 'blue', 'green', 'yellow']
while 'green' in colors:
    colors.remove('green')
print(colors)




print("\n\n---->Now doing list methods pop")
#Unlike remove, when you do a pop it also returns a member of the list.
print("---> Now we are popping the last element")
fruits = ['apple', 'banana', 'cherry', 'date']
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

print("---> You can also specify the position where to pop")
numbers = [10, 20, 30, 40, 50]
removed = numbers.pop(2)
print("removed is: ",removed, " remaining is: ",numbers)

print("---> If you do pop with a matrix it removes the list as it was one member")
matrix = [[1, 2], [3, 4], [5, 6]]
removed = matrix.pop()
print("Removed is: ",removed, " Remaining is: ",matrix)







































































