#COUNTING WITH DICTIONARIES 
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

#DICTIONARY TRACEBACKS
#It is an error to reference a key which is not int he dictionary
#We can use the in operator to see if a key is  in the dictionary
'''
cd = dict()
print(cd['csev'])
This code returns the following error:
print(cd['csev'])
          ~~^^^^^^^^
KeyError: 'csev'
'''

#Back to counting
#When we see a new name we need to add a new entry in the dictionary
print()
print("Counts")
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names : 
    if name not in counts:
        counts[name] = 1
    else : 
        counts[name] = counts[name]  + 1
print(counts)

#The get method in dictionaries
#This method checks if a key is present in the dictionary
#If yes, returns the value
#If no, returns a default value
a = counts.get('csev', 0)
print("csev", a)
a = counts.get('bob', 0)
print("bob", a)
#This method doesn't traceback if key is not there

#Simplified counting with get
counter = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'john', 'zqian']
print()
print(names)
for name in names : 
    counter[name] = counter.get(name, 0) + 1
print(counter)