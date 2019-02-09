import re

#正则表达式对字符串提取，匹配有用...每个字符都有意义。 
#C


#hand = open（'mbox-short.txt'）#for line in hand：#line = line.rstrip（）#Look通过这一行并找到该字符串'From：'。 #if re.search（'From：'，line）：＃如果它在那里，你会得到一个真实的，如果不是，你会得到一个假的。 #print line #Print出在某处有字符串'From：'的行.

        
#当我们在搜索字符串中添加特殊字符时，会出现正则表达式的强大功能#that允许我们更精确地控制哪些行匹配字符串。 ＃将这些特殊字符添加到正则表达式中，允许我们在编写非常少的代码时进行复杂的#matching和提取.

#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    if re.search('^From:', line):       #Now we will only match lines that START with the string 'From:'
#        print line 

#hand = open('mbox-short.txt')
#for line in hand:                       
#    line = line.rstrip()
#    if re.search("^F..m",line):         #Match any line that begins with a four letter word that
#        print line                      #Starts with F and ends with m. 
        
#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    if re.search('^From:.+@', line):    #Match lines that start with "From:" followed by one or more characters (".+")
#        print line                      #before the @ sign. The following will match: From: stephen.maq@uct.ac.za
                                        #Think of .+ as a wildcard that expands to match all characters between
                                        #the colon character and the at-sign. 

#We can use the findall method to find lines with email addresses in them and 
#to extract one or more addresses from each of those lines

#s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM' 
#lst = re.findall('\S+@\S+', s)
#print lst

#We look for substrings that have at least one non-whitespace
#character, followed by an at-sign, followed by at least one 
#one more non-whitespace character. The \S+ matches as many non-whitespace
#characters as possible. 

#it doesnt match the string @2PM because there are no non-blank characters before @

#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.strip()
#    x = re.findall('\S+@\S+', line)
    #print x                             #Find all returns an empty list when the program doesn't find a match
#    if len(x) > 0:
#        print x

# Program above does the following:
#read each line, extract matches, print only lists with at least one substring match
#we get a list of a ton of emails, but some include semi-colons and <. To get rid of 
#the characters we don't want, we use square brackets 

#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#    if len(x) > 0:
#        print x
        
#We fine tuned the program. We are now looking for substrings that
#start with a SINGLE lowercase letter, uppercase letter, or number,
#followed by zero or more non-blank characters
#followed by an at-sign
#followed by zero or more non-blank characters
#followed by an uppercase or lowercase letter

#Create a regular expression that extracts lines that begin with X-

#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    if re.search('^X\S*: [0-9.]+', line):
#        print line
        
#the regular expression says we want lines that:
#start with X-
#followed by zero or more characters .*
#followed by a colon :
#followed by a space
#followed by one or more characters that are either a digit 0-9 or a period [0-9.+]

#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    x = re.findall('^X-\S*: ([0-9.]+)', line)
#    if len(x) > 0 :
#        print x
        
#instead of calling search function, we add parentheses around part of the 
#regular expression that represents the floating-point number to indicate
#we only want findall to give us back the floating point number portion 
#of the matching string

#Try to extract the last digits of this string 
#Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
#from the mbox-short.txt file 

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)
        
#extract for me the part that went in between parentheses. 
#remember, The "+" matches at least one character and the "*" matches zero or more characters

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall( '\S+?@\S+', x)
print(y)
