#Write a program to read through the mbox-short.txt 
#and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address 
#to a count of the number of times they appear in the file. 
#The program reads through the dictionary using a maximum loop to find the most prolific committer.

filename = input("Enter name of text file")
if len(filename) <  1:
    filename = "mbox-short.txt"
filehandle = open(filename)
senders = dict()
for line in filehandle:
    #if the line isn't beginning with From we will simply ignore it
    if not line.startswith('From ') :
        continue
    #Split the line into its constitutent words
    words = line.split()
    #Second word in the line is sender's mail 
    #Using get to crate dictionary of the senders and their frequencies
    senders[words[1]] = senders.get(words[1], 0) + 1
#Now, to find the most freuqent
bigword = None
bigcount = None
for word, count in senders.items():
    if bigcount is None or count>bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)