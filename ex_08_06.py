#Problem Statement
#Look for lines that begin with From
#Print 3rd word

#Initital code that was giving traceback
han = open('mbox-short.txt')
'''
for line in han:
    line = line.rstrip()
    wds = line.split()
    print("Words: ", wds)
    if wds[0] != 'From' :
        print('Ignore')
        continue
    print(wds[2])
'''
#The above code throws a tracebakc for IndexError: List index out of range



for line in han:
    #If there are no words on the line, skip it
    line = line.rstrip()
    #print("Line:", line)
    #Guardian pattern method 1
    '''
    if line == '' :
        print("Skip blank")
        continue
    '''
    wds = line.split()
    #print("Words: ", wds)
    #guardian pattern method 2
    '''if len(wds)<1 :
    #stronger guardian
    if len(wds) < 3 :
        continue
    ''' 

    #Guardian in a compound statement
    if len(wds)<3 or wds[0] != 'From' :
        #here the order is imp
        #guardian comes before condition 
        #print('Ignore')
        continue
    print(wds[2])