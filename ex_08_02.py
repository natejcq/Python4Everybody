#MANIPULATING LISTS
#operations that you can do with lists

#Adding / Concatenating using +
a = [1, 3, 5]
b = [2, 5, 0]
print("a is", a, "\nb is", b)
c = a+b
print("c is", c)

#Slicing lists using :
#Note: Upto but not including4
t = [9, 41, 12, 63, 94, 15]
print("\nt is", t)
print("t[1:3] is", t[1:3])
print("t[:4] is", t[:4])
print("t[3:] is", t[3:])

#Consider a list
nums = [3, 41, 12, 9, 74, 15]
print("\n", nums)
#append method adds an object to the end of the list
#len tells you how many things are in a list
print("Length of nums is", len(nums))
#min, masx fund minimum and maximum
print("Maximum element is", max(nums))
print("Minimum element is", min(nums))
#sum will add up all elements of list, works if all elements are numeric in nature
print("Sum of all elements is", sum(nums))
#count tells you how many things that match a particular thing are in a list



#BUILDING A LIST FROM SCRATCH
#We can create an empty list and then add elements using the append method
print()
stuff = list()
print("Stuff is", stuff)
stuff.append('Book')
print("Stuff is", stuff)
stuff.append(99)
print("Stuff is", stuff)
stuff.append('Cameras')
print("Stuff is",stuff)
#The list stays in order, new elements inserted at end of list

#IS SOMETHING IN A LIST?
some = [1, 9, 21, 10, 16]
print()
print("some", some)
print("Is 9 in some?")
print(9 in some)
print("Is 20 not in the some?")
print(20 not in some)

#LISTS ARE IN ORDER
#A list can hold many items and keeps those items in the order until we do something to change the order
#A list can be sorted
friends  = ['Glen', 'Jospehine', 'Sally']
print()
print("Friends", friends)
friends.sort()
print("Friends on sorting", friends)

#Calculating average using two methods
#Method 1
total = 0
count = 0 
while True:
    inp = input("Enter a number")
    if inp == 'done' :
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)
#Method 2
numlist = list()
while True:
    inp = input("Enter a number")
    if inp == 'done' : 
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)
#Method 1 keeps only current number in memory
#Method 2 keeps all numbers stored in memory
#Sometimes, amount of memory usage matters (not here since not dealing w lots of data) 