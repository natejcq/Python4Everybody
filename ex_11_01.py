#REGULAR EXPRESSIONS
'''
In computing, a regular expression, also referred to as "regex" or "regexp", provides a concise and flexible means for matching strings of text, such as particular characters, words or patterns of characters
A regular expression is written in a formal language that can be interpreted by a regular expression processor
From the 1960s to today, a lot of operating systems have used regular expressions as a more efficient method for search
Regular expressions : Really clever "wild card" expressions for parsing and matching strings
'''

#UNDERSTANDING REGULAR EXPRESSIONS
'''
Very powerful and cyptic
Fun once you understand them 
Regular expressions are a language unto themselves
A language of "marker characters" - programming with characters
Its kind of an "old school" language - compact
'''

#REGULAR EXPRESSIONS QUICK GUIDE
'''
^        matches the beginning of a line
$        matches the end of a line'
.        matches any character
\s       matches any whitespace
\S       matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The seet of characters can include a range 
(        Indicates where the string extraction is to start   
)        Indicates where the string extraction is to end
'''

#THE REGULAR EXPRESSION MODULE
'''
~ Before you can use regular expressions in your program, you must import the libarary using "import re"
~ You can use re.search() to see if a string matches a regular expression
~ You can use re.findall() to extract portions of a string that match your regular expression
'''

#Using re.search() like find()
'''
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >= 0 :
        print(line)
'''
import re
hand2 = open('mbox-short.txt')
for line in hand2:
    line = line.rstrip()
    if re.search('From: ', line) : 
        print(line)

#Wild - card charcters
#The dot matches any character
print()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
#This will match anything that starts with X and has a colon later 
    if re.search('^X.*:', line):
        print(line)
