#SLICING STRINGS
s = "Monty Python"
print("String s is", s)
print("0:4 is",s[0:4])
print("6:7 is", s[6:7])
print("6:20 is", s[6:20])
#Note : it is not always nececssary to give start index, assumed 0
#       it is not always necessary to give ending index, assumed end of string
print(":2 is", s[:2])
print("8: is", s[8:])

#Some string library functions
str = "Hello Bob"
#full lowercase
lstr = str.lower()
#full uppercase
ustr = str.upper()
print(str)
print(lstr)
print(ustr)
str1 = 'ada lovelace'
print(str1)
#capitalize first letter
print(str1.capitalize())
#capitalize first letter of every word
print(str1.title())

#Searching in a string using 'find'
fruit = 'banana'
pos = fruit.find('na')
print("Position of \'na\' in", fruit, "is", pos)
aa = fruit.find('z')
pos2 = fruit.find('z')
print("Position of \'z\' in", fruit, "is", pos2)
#find() returns -1 if not found

#Search and replace strings in Python
greet = 'Hello Bob'
print("Greet is", greet)
newgreet = greet.replace('Bob', 'Jane')
#replaces Bob with Jane in greet
print("newgreet is", newgreet)
newgreet2 = greet.replace('o', 'X')
print("newgreet2 is", newgreet2)

#Stripping whitespaces
#lstrip() and rstrip() will strip off aany whitespaces to the left or right of the string 
#strip() removes both beginning and ending whitespaces

#Prefixes
line = 'Please have a nice day'
print(line)
res = line.startswith("Please")
print(res)
