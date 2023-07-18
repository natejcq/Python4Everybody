#Looping through a string in Python
fruit = 'banana'
#definite loop
for letter in fruit : 
    print(letter)

#indefinite loop
index = 0
while index < len(fruit) : 
    letter = fruit[index]
    print(index,letter)
    index = index  + 1 

#SIMPLE LOOP TO COUNT THE OCCURENCE OF A SPECIFIC LETTER IN A STRING
word = input("Enter a word : ")
count = 0
for letter in word : 
    if letter == 'e' : 
        count = count + 1
print("The letter e occurs", count, "times in", word)

#Using "in" as a logical operator
fruits = 'bananas'
print("Fruits is", fruits)
print("n in fruits", 'n' in fruits)
print("m in fruits", 'm' in fruits)

#concatenating strings
a = "hello"
b = "there"
print("a+b is", a+b )
print("a,b is")
print(a,b)
#Note : Concatenation does NOT add a space 
