#TUPLES
#Tuples are anotehr kind of sequence that functions much like a list - they have elements which are indexed starting at zero

x = ('Glen', 'Sally', 'Joseph')
print(x[2])
y=(1,9,2)
print(y)
#iterating through a tuple
for iter in y:
    print(iter)

#Tuples are immutable. 
#Once you create a tuple, you cannot alter its contents
'''
Things you cannot do with tuples
1) Sort
2) Append
3) Reverse
All because they are not mutable
'''

# Tuples are more efficient. 
'''
Since Python does not have to build tuple structures to be modifiable, they are simpler and more effivcient in terms of memory use and performance than lists
So in our peogram when we are making 'temporary variables' we prefer tuples over lists
'''

#Tuples and Assignment
#We can put tuples of LHS of assignment statement
(x, y) = (4, 'fred')
print(y)
(a,b) = (98, 99)
print(a)
#We can even omit the parentheses
a,b,c = 1,2,3
print(a, b, c)

#Tuples and Dictionaries
#The items() method in dictionaries returns a list of (key, value) tuples
d = dict()
d['csev'] = 3
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v) 
tups = d.items()

#Tuples are comparable
#The comparison operators work with tuples and other sequences. 
# If the first item is equal, Python goes on to the next element, and so on until it finds elements taht differ
print("Is (0,1,2) less than (5, 1, 2)?")
print((0, 1, 2) < (5, 1, 2)) 
print("Is (0, 1, 200000) less than (0, 3, 4)?")
print((0, 1, 200000) < (0, 3, 4))

#Sorting lists of tuples
#We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary. This performs a sort by key
 
#First we sort the dictionary by key using the items() method and then sorted() function
d = {'a':10, 'c':22, 'b':1}
dict_items = d.items()
print(dict_items)
print("Sorted (based on keys)")
print(sorted(dict_items))
#We can do this even more directly using the function sorted() as it takesa sequence and returns a sorted sequence
e = {12: 'twelve', 1:'one', 19:'nineteen'}
print(e.items())
print("Sorted")
for k, v in  sorted(e.items()) : 
    print(k,v)

#Sorting by value
#If we could construct a list of tuples of the form (value, key), then we can use sorted() method to sort by value
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp)
res = list()
for k,v in tmp:
    res.append((v,k))
print("Sorting by value done")
print(res)