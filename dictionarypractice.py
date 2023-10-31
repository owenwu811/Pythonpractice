mydict = {"a": 1, "b": 2, "c": 3}
for i, j in mydict.items():
    print(i, j)
#output a 1 b 2 c 3

for x in mydict.values():
    print(x)
#output: 1 2 3

for a in mydict:
    print(a)
#output: abc

mydict.pop("a")
print(mydict)
#output: {'b': 2 'c': 3}

#removing item in a set:
x = {1, 2, 3, 4, 5}
x.discard(3)
print(x)
#output: 1245

a = {'a', 'b', 'c'}
a.discard('b')
print(a)
#output ac

#using set constructor to create a set:
myset = set(('a', 'b', 'c', 'd'))
print(myset)
myset.clear()
print(myset)
#del myset - this will cause line after to throw an error since the set no longer exists
#print(myset)

h = tuple((1,2,3,4,5)) #works with integers, not just strings
print(h)
if 2 in h:
    print("2 is inside the h tuple")
print(len(h))

#pop method in set to get last element
myset = {1,2,3,4,5,6,7,8,9,10}
a = myset.pop() #removes random item since set order is scrambled and random!
print(a) #prints the removed item itself - 1 in this case
print(myset)
#set removes duplicates, so only one 4 will show:
mysettwo = {'h', 'y', 4, 4, -1.0000}
operation = mysettwo.pop()
print(operation) #'h'
print(mysettwo) # y 4 -1.0000

e = {999, -11.0, 'r', 'r', 't', 'w'}
operationtwo = e.pop()
print(operationtwo)
print(e)

a = {1, '2', 3, 3, 3, 4}
h = a.pop()
print(h)
print(a)

g = {4, 4, 4, 'a', 5}
j = g.pop() #since set order dosen't matter, a random number is popped + sets remove duplicates!!!!! - POP REMOVES A RANDOM ITEM FROM A SET SINCE ORDER DOSEN'T MATTER!!!!!
print(g)
print(j)


j = {'a':1, 'b':2, 'c': 3}
print(j.clear())

#output: None

import math
j = 5.4
print(math.ceil(j))

#output: 6

a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print('b' in a)

#output: true
