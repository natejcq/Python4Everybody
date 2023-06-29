#LISTS AND STRINGS
#This class focuses on how lists abd strings work together

#split() can be used to convert one string into a list of strings
#We can access a particular word or loop through all the words
abc = 'With three words'
print(abc)
stuff = abc.split()
print("After split", stuff)
print("Looping to access words: ")
for w in stuff :
    print(w)
#Split automatically assumes white space to be the delimiter.Multiple whitespaces are treated same as one
a = 'A lot        of spaces'
print(a)
stuff1 = a.split()
print(stuff1)
#We can specify our own delimiter character to use in the splitting
line = 'first;second;third'
print(line)
thing = line.split(';')
print(thing)

print()
print("Days of the week in mbox-short.txt")
#Using split on mail-data
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
    print(words[2])

#The Double split pattern
#Sometimes we split a line one way and then grab one of the pieces of the line and split that again
print()
print("Domains of e-mail")
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])