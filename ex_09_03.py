#Dictionaries and files

#The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of the words independently
count = dict()
print("Enter a line of text")
line = input(' ')
words = line.split()
print("Words: ", words)
print('Counting......')
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

#definite loops and dictionaries
#Even though dictionaries are not stored in order we can write for a loop that goes through all the entries in a dictionary - actually it goes through all of the keys and looks up the values
print()
jjj = {'chuck':1 , 'fred':42, 'jam':100}
for key in jjj:
    print(key, jjj[key])

#Retrieving a list of keys and values
#You can get a list of keys, values or items(both) from a dictionary
print()
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())
#jjj.tems is a list of tuples

#Using two iteration variables
#We loop throughg the key-value pairs in a dictionary using two iteration variables
#Each iteration, the first variable is the key and the second variable is the corresponding value for the key
for aaa, bbb in jjj.items() :
    print(aaa, bbb)

print()
#Read a file of text, find most common word , its frequency
name = input('Enter file name: ')
if len(name)<3:
    name = 'words.txt'
fh = open(name)
counts = dict()
#Create a list of all words, their frequencies
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1  
#Now we start finding the largest one
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount : 
        bigcount = count
print(bigword, bigcount)