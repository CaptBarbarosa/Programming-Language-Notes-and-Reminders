""" 
Please know that I'm also very well aware that it is stupid to memorize these stuff, 
yet I believe knowing they exists will come handy.
"""

                ###   LIST    ###


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

                ###   METHODS    ###

print("\n\n---->Now doing list method: append")
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





print("\n\n---->Now doing method: extend")
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

print("---> Extending a dictionary")
data = {
    "numbers": [1, 2, 3],
    "letters": ["a", "b"]
}
data["numbers"].extend([4, 5, 6])
data["letters"].extend(["c", "d"])
print(data)

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





print("\n\n---->Now doing the method: copy")
#Please note that copy works with dictionaries and tuples too.
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

print("---> You can specify the index")
fruits = ('apple', 'banana', 'cherry')
for index, fruit in enumerate(fruits, start=1): 
    print(f"Index: {index}, Fruit: {fruit}")

print("---> You can create a list with enumerate")
squares_with_indices = [(index, num**2) for index, num in enumerate(range(1, 6))]
print(squares_with_indices)

print("---> You can create a dictionary with enumerate")
items = ['apple', 'banana', 'cherry']
indexed_dict = {index: item for index, item in enumerate(items)}
print(indexed_dict)





print("\n\n---->Now doing list methods: map")
# Please notice the similarities with this and loops
print("---> Mapping a list")
numbers = [1, 2, 3, 4, 5]
mapped = map(str, numbers)
result = list(mapped)
print(result)

print("---> Mapping with a lambda function")
squared = map(lambda x: x**2, numbers)
result = list(squared)
print(result)

print("---> Operations within a map")
numbers2 = [4, 5, 6]
summed = map(lambda x, y: x + y, numbers, numbers2)
result = list(summed)
print(result)

points = [(1, 2), (3, 4), (5, 6)]
first_elements = map(lambda point: point[0], points)
result = list(first_elements)
print(result)





print("\n\n---->Now doing list methods: filter")
# Please notice the similarities with this and loops
print("---> It is like if but better")
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
long_words = filter(lambda x: len(x) > 5, words)
result = list(long_words)
print(result)

print("---> You can do it with tuples")
numbers = (10, 15, 20, 25, 30, 35, 40)
greater_than_25 = filter(lambda x: x > 25, numbers)
result = list(greater_than_25)
print(result)

print("---> Or you can do it with dictionaries")
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28}
]
adults = filter(lambda person: person['age'] > 28, people)
result = list(adults)
print(result)


nums = [4,2,6,13,30,42]
my_list = filter (lambda n: n%2 == 0, nums)
print(list(my_list))

average = sum(nums)/len(nums)
higher_than_average = list(map(lambda n: n*n, filter (lambda num: num > average, nums)))
print(higher_than_average)





my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)



                ## String Methods
print("\n\n---->Now doing string methods: slice")
my_string = "Hello Mate"
my_string = my_string[2:5]
print(my_string)

print("\n\n---->Now doing string methods: strip")
print("With string stripping you can dismiss characters from a string")
my_string = "   Hello Mate  "
print(my_string.strip())
my_string = "#Hello Mate###"
print(my_string.strip("#"))

var: str = 'var'
print(f'{var:>10}') # There will be a leftward expansion for 10 characters.

print("You can remove given characters from the strings as well.")
my_string = "www.examplec.com".strip('cmow.')
print(my_string) # Please notice that it also removed c from examplec





print("\n\n---->Now doing string methods: removesuffix, removeprefix")
my_string = "Arthur: Hello there Arthur: ".removeprefix('Arthur: ')
print(my_string)

my_string = "HelloPython".removesuffix("Python")
print(my_string)





print("\n\n---->Now doing string methods: replace")
my_string = "Lets do an exercise on replace".replace(' ','_')
print(my_string)



                   ###   Some methods used in dictionaries   ###

print("\n\n---->Now doing dictionary methods: fromkeys")
# fromkeys method is used to create a new dictionariy with the keys from a given sequence.
# Usage: dict.fromkeys(sequence, value)

keys = ['a', 'b', 'c']
my_dict = dict.fromkeys(keys)
print(my_dict)
print("---> Or you can specify the value.")
given_value = 3
my_dict = dict.fromkeys(keys,given_value)
print(my_dict)

print("---> If you have a string, the fromkeys method create  a dictionary item from each of them")
keys = 'abc'
given_value = 3
my_dict = dict.fromkeys(keys, given_value)
print(my_dict)

print("---> If you used tuples as keys, they are immuted.")
keys = [('a', 1), ('b', 2), ('c', 3)]
given_value = 'Value'
my_dict = dict.fromkeys(keys, given_value)
print(my_dict)





print("\n\n---->Now doing dictionary methods: get")
# With "get" method you retrieve the values associated with a given key.
# Usage: dict.get(key, default_value)
my_dict = {'a' : 1, "b" : 2, 'c' : 3}
value = my_dict.get('b')
print(value)

print("---> If the key doesn't exists you can either get default NONE or the value you specified.")
value = my_dict.get('d')
print(value)
value = my_dict.get('d',4)
print(value)





print("\n\n---->Now doing dictionary methods: items")
""" 
Items returns a view object that displays a list of a dictionary's key tuple pairs.
It allows to iterate over the keys and values in the dictionary.
"""
# Usage: dict.items
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
items = my_dict.items()
print(items)

print("---> Turning it into list can help")
items = list(items)
print(items)

print("---> Or you can iterate in the loop")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")





print("\n\n---->Now doing dictionary methods: keys")
# It is like a version of items that only shows keys. It returns keys
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
keys = my_dict.keys()
print(keys)





print("\n\n---->Now doing dictionary methods: values")
# It is like a version of items that only shows values. It returns keys
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
values = my_dict.values()
print(values)





print("\n\n---->Now doing dictionary methods: pop")
# It pops a given key. If the key is not present it gives a 'KeyError'
# Usage: dict.pop(key, deafult) Please note that default is optional and exists so that the program doesn't crash
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
value_popped = my_dict.pop('c')
print(value_popped)
print(my_dict)
my_dict['c'] = 3 # Pushed the popped value back
#value_popped = my_dict.pop('d') # If this code is run, it will give an error
value_popped = my_dict.pop('d',-1)
print(value_popped)
print(my_dict)





print("\n\n---->Now doing dictionary methods: popitem")
# It pops the last element
key, value = my_dict.popitem()
print(f"Removed item: ({key}, {value})")
print(my_dict)



"""
# Or you can use setdefault
print(my_dict)
key = str(input("Enter key: "))
value = input("Enter value: ")
if key not in my_dict:
    my_dict[key] = value
else:
    print(my_dict[key])
print(my_dict)
"""











































