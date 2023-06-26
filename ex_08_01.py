#A list is a kind of collection
#A collection is nice because we can carry many values around in a ssingle container

#friends is a list made up of three strings
friends = ['Jospeh', 'Glen', 'Sally']
#Similarly, carryon is also a list of strings
carryon = ['socks', 'shirt', 'perfumes']

#List constants are surrounded by square brackets and the elements in the list are seperated by commas
#A list element can be any python object, even another list

#This list contains one list and two integers
mylist1 = [1, [5, 6 ,7], 12]
#This list has three elements: one string, one integer, one float  
mylist2 = ['red', 24, 98.64]

#for loops and lists: Best pals
z = ['Krish', 'Sanika', 'Mamta']
for x in z : 
    print("Good evening", x)
print("Done")
print()

#Looking inside lists
print(friends)
print("Second element of list is",friends[1])
print()

#LISTS ARE MUTABLE
#We can change the elements of a string using the index operator
lotto = [2, 14, 26, 41, 63]
print("List is",lotto)
lotto[2] = 33
print("After list[2] = 33", lotto)
print()

#Length of a list
#The len() function takes a list as a parameter and returns number of elements
list1 = [1,2,3,45,2,3,542,23,2,42,45,25,342,423,42,342,32]
print(list1)
print("length is: ", len(list1))

#Using the range function
#The range function returns a list of numbers starting from zero to one less than the parameter

#Method 1 
for number in list1 :
    print(number)

#Method 2
for i in range(len(list1)):
    number = list1[i]
    print(number)