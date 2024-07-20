""" 
Please know that I'm also very well aware that it is stupid to memorize these stuff, 
yet I believe knowing they exists will come handy.
"""

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




print("\n\n---->Now doing list methods: insert")
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




print("\n\n---->Now doing list methods: remove")
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




print("\n\n---->Now doing list methods: pop")
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





print("\n\n---->Now doing list methods: clear")
# With clear you can emtpy the entire lists.
fruits = ['apple', 'banana', 'cherry', 'date']
fruits.clear()
print(fruits)





print("\n\n---->Now doing list methods: index")
print("---> You can find index of a given member from the list")
# If it exists more than one time it shows the first occurence.
fruits = ['apple', 'banana', 'cherry', 'date', 'cherry']
index_cherry = fruits.index('cherry')
print(index_cherry)

print("---> You can specify which indexes to look between")
letters = ['a', 'b', 'c', 'b', 'd', 'b']
index_b = letters.index('b', 2) # Looks after index 2
index_b_range = letters.index('c', 2, 5) #Looks within 2 and 5
print("First: ",index_b, " Second: ",index_b_range)





print("\n\n---->Now doing list methods: count")
print("---> With count you can count how many occurance an element has within a list")
numbers = [1, 2, 'Apple', True, 3, 2, 4, 2, 5]
twos = numbers.count(2)
print("Number of twos are: ",twos)




print("\n\n---->Now doing list methods: sort")
print("---> You can sort normally, or reverse")
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print("----> Reversely sorted version is\n" ,numbers)

print("---> In strings it sorts alphabetically")
fruits = ['banana', 'apple', 'cherry', 'date']
fruits.sort()
print(fruits)

print("---> In tuples or dictionaries within list you have to specify yourself")
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]
students.sort(key=lambda x: x[1], reverse = True)
print(students)
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}]
people.sort(key=lambda x: x['age'])
print(people) 





print("\n\n---->Now doing list methods: copy")
import copy
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shallow_copy = copy.copy(original)
original[0][0] = 99
print("!!---> In shallow copy the changes you make in one shows in other")
print("Original: ", original)
print("Shallow Copy: ", shallow_copy)

original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep_copy = copy.deepcopy(original)
original[0][0] = 99
print("!!---> In deep copy the changes you make in one doesn't shows in other")
print("Original: ", original)
print("Shallow Copy: ", deep_copy)





print("\n\n---->Now doing list methods: enumerate")
# With enumerate we can loop over a list and have an automatic counter. 
# Enumerate returns an enumerate object, which can then be converted into a list of tuples.
"""
enumerate(iterable, start=0)
iterable = Any iterable object such as a list, tuple, dictionary or string.
"""

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")


















