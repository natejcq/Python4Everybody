#GRADED EXERCISE 5.2
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and 
#put out an appropriate message and ignore the number. 
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: 
        number = int(num)
    except:
        print("Invalid Inputs")
        continue
    if smallest is None : 
        smallest = number
    if largest is None : 
        largest = number
    if number > largest : 
        largest = number
    if number < smallest : 
        smallest = number
    print(num)

print("Maximum", largest)
print("Minimum", smallest)
