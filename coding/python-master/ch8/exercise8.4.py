#打开文件romeo.txt并逐行读取。 ＃对于每一行，使用split（）方法将该行拆分为单词列表 
#该程序应该构建一个单词列表。对于每行上的每个单词，请检查#if该单词是否已在列表中，如果没有将其附加到列表中。 ＃当程序完成时，按字母顺序对生成的单词进行排序和打印.


fhand = open('romeo.txt')           #open file name
lst = list()                        #create an empty list

for line in fhand:                  #For loop traverses each line in file. Next, for each line
	splitz = line.split()           #split the line into a list of words using the split function
	print(splitz)                   #The program has built a list of words.
	print(len(splitz))
	for i in range(len(splitz)):    #The range function creates a list and gives it back to us.
																																#It also corresponds to items in splitz list.
		if splitz[i] not in lst:
			lst.append(splitz[i])
			
lst.sort()
print(lst)


