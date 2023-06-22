#Working with Files CH 7 
#Write a program that prompts for a file name, then opens that file and reads through the file
#print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.
fname = input("Enter the file name: ")
try:
    filehandle = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
for line in filehandle :
    line = line.upper()
    line = line.rstrip()
    print(line)