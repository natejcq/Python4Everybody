#Parsing and extracting in strings
#We want to extract the email server used by Stephen 
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#first we find the @ sign
print(data)
atpos = data.find('@')
print("@ sign found at", atpos)
#find next sapce starting search at atpos
sspos = data.find(' ', atpos)
print("Next space after @ found at", sspos)
host = data[atpos+1 : sspos]

#.format()
#replaces placeholder with argument
good = True
question = "AM  I GOOD? {}"
print(question.format(good))

#f-strings in Python
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
donot = "don\'t"
y = f"Those who know {binary} and those who {donot}."
print(f"I said : {x}")
print(f"I also said : {y}")

#Using multiplication causes string to repeat those many times
print('.'*10)
