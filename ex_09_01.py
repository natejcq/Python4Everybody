#DICTIONARIES ARE PYTHON'S MOST POWERFUL DATA COLLECTION
#Dictionaries allow us to do fast database-like operations

#Lists index their entries based on positiions in the list
#Dictionaries are like bags - so no order

#Dictionaries are essentially key-value pairs
#We index things we put in the dictionary with a lookup tag aka key

#Create a dictionary object using its constructor
purse = dict()
#money is the key , 12 is the value
purse['money'] = 12
#candy is the key, 3 is the value
purse['candy'] = 3
purse['tissues'] = 7
print("Purse is: ", purse)

#To access the value use its key
print("Value associated with candy is", purse['candy'])
#Values can also be manipulated
purse['candy'] = purse['candy'] + 3
print("now purse is", purse)

#Comparing dictionaries and lists
#Dictionaries are like lists except they use keys instead of  numbers to look up values
lst = list()
lst.append(21)
lst.append(183)
print("List is",lst)
lst[0] = 23
print("After modifying",lst)
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

#Dictionary literals (constants)
#Dictionary literals usecurly braces and have a list of key : value pairs
#You can make an empty dictionary using empty curly braces
jjj = {'chuck' : 1, 'fred': 42, 'james' : 100}
print(jjj)
ooo = { }
print(ooo)