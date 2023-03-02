''' ************ Questions on Lists ****************** '''

#  Q-1. What will be the output of the following code snippet?

'''a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])'''    #  [1, 3, 5, 7, 9]

# Q-2. What will be the output of the following code snippet?
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[::2] = 10, 20, 30, 40, 50, 60
print(a) '''      # Error Because count of slicing values are higher than the replacing values

# Q-3. What will be the output of the following code snippet?
'''a = [1, 2, 3, 4, 5]
print(a[3:0:-1])'''       # [4, 3, 2]

# Q-4. What will be the output of the following code snippet?
'''def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0]) '''          # 3, 44

# Q-5. What is the correct command to shuffle the following list?
'''fruit=['apple', 'banana', 'papaya', 'cherry']
A. fruit.shuffle()
B. shuffle(fruit)
C. random.shuffle(fruit)
D. random.shuffleList(fruit)  '''        # random.shuffle(fruit) or random.choice(fruit)

# Q-6. What will be the output of the following code snippet?
'''data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]           # v = 1

    for row in m:        # m =  [1, 2], [3, 4]
        for element in row:      # row = [1, 2, 3, 4]
            if v < element: v = element

    return v
print(fun(data[0]))  '''     # 4

# Q-7. What will be the output of the following code snippet?
'''arr = [[1, 2, 3, 4],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]]
for i in range(0, 4):
     print(arr[i].pop())  '''    # Pop() is used to return the removed value. 4, 7, 11, 15


# Q-8. What will be the output of the following code snippet?
'''def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)    '''      # [1] [1, 2] [1, 2, 3]

# Q-9. What will be the output of the following code snippet?
'''arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]        # [2, 3, 4, 5, 6, 6]
for i in range(0, 6):
    print(arr[i], end = " ") '''      #  [2, 3, 4, 5, 6, 6]


# Q-10. What will be the output of the following code snippet?
'''fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1         # Deep Copy
fruit_list3 = fruit_list1[:]      # Shallow Copy

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print (sum)'''

''' ************ Questions on Tuples ****************** '''

# Q-1. What will be the output of the following code snippet?
'''init_tuple = ()
print(init_tuple.__len__())    # 0 (length of empty tuple is  always Zero)'''

# Q-2. What will be the output of the following code snippet?
'''init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print (init_tuple_a == init_tuple_b)'''   # True (Same Address)

# Q-3. What will be the output of the following code snippet?
'''init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print(init_tuple_a + init_tuple_b) '''        # ("1", "2", "3", "4")


# Q-4. What will be the output of the following code snippet?
'''init_tuple_a = 1, 2
init_tuple_b = (3, 4)
[print(sum(x), type(x)) for x in [init_tuple_a + init_tuple_b]]'''

# Q-5. Add the First values in a Tuple.
'''data = [(0, 1), (1, 2), (2, 3)]
result = (sum(i for i, _ in data))
print(result)'''

# Q-6. Add the Last Values ina Tuple.
'''data = [(0, 1), (1, 2), (2, 3)]
result = (sum(i for _, i in data))
print(result)'''

# Q-7. Which of the following statements given below is/are true?
'''A. Tuples have structure, lists have an order.
B. Tuples are homogeneous, lists are heterogeneous.
C. Tuples are immutable, lists are mutable.
D. All of them.'''   # A & C

# Q-8. What will be the output of the following code snippet?
'''init_tuple = ('Python') * 3
print(type(init_tuple)) '''        # String Type

# Q-9. What will be the output of the following code snippet?
'''init_tuple = (1,) * 3

init_tuple[0] = 2

print(init_tuple)  '''     # Tuple Object doesn't have Item Assignment. So, the result is Type Error.

# Q-10. What will be the output of the following code snippet?
'''init_tuple = ((1, 2),) * 7        # ((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))

print(len(init_tuple[3:8]))'''       # 4

''' ************** Questions on Dictionaries **************'''
# Q-1. What will be the output of the following code snippet?
'''a = {(1,2):1,(2,3):2}
print(a[1,2]) '''             # 1

# Q-2. To Display the occurance of the items of a tuple in Dictionary Format
'''x = (1, 2, 3, 4, 2, 2, 1, 2, 5)
y = {}
for item in x:
    if item in y:
        y[item] += 1
    else:
        y[item] = 1
else:
    print(y)'''           # {1 : 2, 2 : 4, 3 : 1, 4 : 1, 5 : 1}
# Q-4. What will be the output of the following code snippet?
'''arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1
sum = 0
for k in arr:               # {1 : 2}, '1' : 2}
    sum += arr[k]

print (sum)'''             # 4


# Q-5. What will be the output of the following code snippet?
'''my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
print(my_dict)
sum = 0
for k in my_dict:
    sum += my_dict[k]        # {1 : 4, '1' : 2}

print(sum)'''                # 6

# Q-6. What will be the output of the following code snippet?

'''my_dict = {}
my_dict[(1, 2, 4)] = 8
my_dict[(4, 2, 1)] = 10
my_dict[(1, 2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)                   # 30
print(my_dict)'''            #  {(1, 2, 4) : 8, (4, 2, 1) : 10, (1, 2) : 12}

# Q-7. What will be the output of the following code snippet?
'''box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates[box]))'''          # Un-hashable Type Errors

# Q-8. What will be the output of the following code snippet?
'''dict = {'c': 97, 'a': 96, 'b': 98}

for _ in sorted(dict):
    print (dict[_], end=" ")'''      # 96 98 97

# Q-9. What will be the output of the following code snippet?
'''rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
print(id(r) == id(rec))'''           # False (.copy and Slicing assignment of two variables is always false)


# Q-10. What will be the output of the following code snippet?
'''rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)   '''                   # True



