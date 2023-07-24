fname = input('Enter File: ')
try:    
    fhand = open(fname)
except:
    print("Incorrect filename, run again")
di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        #Simple one line method
        di[w] = di.get(w,0) + 1
#        print(w, 'new', di[w])
#print(di)

#Now we want to find the 5 most common words
#For that we need to sort the frequencies and print top 5
#But our sorted() works on the foirst instance of the tuple

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)
    #Equivalent to  tmp.append((v,k))
    #So now we have a list that has frequencies as values, words as keys
#print("Flipped")
#print(tmp)
di_fin = dict()
#Sort is in ascending by default
di_fin = sorted(tmp, reverse=True)
#print("Sorted")
#SInce we need only top 5 most common 
print(di_fin[:5])

for v,k in di_fin[:5]:
    print(k, v)
