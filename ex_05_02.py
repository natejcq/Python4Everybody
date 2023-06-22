#Write a program which repeatedly reads numbers until the user enters "done". 
#Once "done" is entered, print out the total, count, and average for the numbers
#If the user enters anything other than a number, detect their mistake using a try and except, print error message and skip to the next number
total = 0.0
count = 0 
while True :
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue
    count = count + 1 
    total = total + fnum
print("ALL DONE")
print("TOTAL IS :", total)
print("COUNT IS :", count)
print("AVERAGE IS :", total/count)