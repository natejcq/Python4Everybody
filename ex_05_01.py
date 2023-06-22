#Simple loop
n = 5
while n>0 : 
    print(n)
    n = n-1
print("Blastoff")
print(n)

#Infinite loop (DO NOT DO)
#n = 5
#while n>0 : 
#    print("Lather")
#    print("Rinse")
#
#print("Dry off")

#Finding average in a loop
total = 0
count = 0
print('Before', count, total)
for thing in [9, 41, 12 , 3, 74, 15] :
    count = count + 1
    total = total + thing
    print(count, total, thing)
print("After", count, total)
print("Average is", total / count)

#Filtering in a loop
print('Before')
for value in [9, 41, 12, 3, 74, 15] : 
    if value > 20 : 
        print(value, " is greater than 20")
print("After")

#If atleast one occurence of 3 return true
found = False
print('Before', found)
for value in [9,41, 12, 3, 74, 15] : 
    if value == 3 :
        found = True
    print(found, value)
print('After', found)

#Optimizing above code with break
found = False
print('Before', found)
for value in [9,41, 12, 3, 74, 15] : 
    if value == 3 :
        found = True
        break
    print(found, value)
print('After', found)

#Finding smallest value
smallest_so_far = 100
print('Before', smallest_so_far)
for value in [9, 41, 12, 3, 74, 15] : 
    if value < smallest_so_far :
        smallest_so_far = value
    print(smallest_so_far, value)
print('After', smallest_so_far) 

#Some optimization
smallest_so_far = None
#it is always important to use this since we don't always have a literal to use in order for initialization
print('Before', smallest_so_far)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None : 
        smallest_so_far = value
    elif value < smallest_so_far : 
          smallest_so_far = value
    print(smallest_so_far, value)
print('After', smallest_so_far) 