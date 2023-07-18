#Ten most common words

fname = input("Enter file name: ")
if len(fname) < 3 : 
    fname = 'romeo.txt'
try:
    fhand = open(fname)
except:
    print("Cannot open file, sorry.")
    print("Run me again")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

#Line 17 to 24 can be done in one line of code as follows:
'''
print(sorted([(v,k) for k,v in counts.items()]))
1.
    (v,k) for k,v in counts.items()
    First convert counts into a list of tuples
    then swap the key and value in those tuples
2.
    pass that list of tuples into the sorted() function
    Gives a sorted list of tuples
3.
    If you want key first and then function you can reverse this again
'''