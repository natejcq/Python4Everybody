'''
PROBLEM STATEMENT:
Write a program to read through the mbox-short.txt and  figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time  and then splitting the string a second time using a colon.  
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
fname = input("Enter file name: ")
if len(fname)<3 :
    fname = 'mbox-short.txt'
try:
    fhandle = open(fname)
except:
    print("Could not open file please run again")

#Create a new dictionary
di = dict()

for line in fhandle:
    #If line doesn't start with From simply move on 
    if not line.startswith('From '):
        continue
    #Else split the line 
    words = line.split(' ')
    #print(words)
    #We can see that the time stamp is the 7th item in list at index 6
    #Now, for every line we will simply find the 7th word and split it again on colon 
    ts = words[6].split(':')
    #print(ts)
    #the 1st part of this timestamp will give us hour
    hr = ts[0]
    di[hr] = di.get(hr, 0) + 1
#This should create and give us a dictionary with all the hours as keys and frequencies as values
#print(di)
#Next we shall sort. For sorting first convert dictionary into a list of tuples 
l = di.items()
#Then sort the tuples based on hour 
lsorted = sorted(l)
for k,v in lsorted:
    print(k, v)