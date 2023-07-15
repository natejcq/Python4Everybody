fname = input('Enter File: ')
if len(fname) < 1 :
    fname = 'clown.txt'
fhand = open(fname)
di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        #Simple one line method
        di[w] = di.get(w,0) + 1
#        print(w, 'new', di[w])
#Long verbose method
'''
        if w in di :
            di[w] = di[w] + 1
            print("**Existing**")
        else:
            di[w] = 1
            print("**New**")
'''

#Slightly better, shorter method
'''
        #if key not there count is zero
        oldcount = di.get(w,0)
        print(w,'old', oldcount)
        newcount = oldcount+1
        di[w] = newcount
        print(w, 'new', newcount)
'''
print(di)
#Now we want to find the most common word
#i.e. a maximum loop
largest = -1
mcw = None
for k,v in di.items() :
    if v > largest:
        largest = v
        mcw = k
print('Done', mcw, largest)