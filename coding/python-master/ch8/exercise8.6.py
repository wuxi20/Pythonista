#练习8.6重写程序，提示用户输入数字列表，并在用户输入完成后输出最终和最小数字。 #Write程序存储用户在列表中输入的数字，并使用max（）和min（）函数＃计算循环完成后的最大和最小数字.

smallest = None
largest = None
lst = list() #create an empty list

while True:

	userinp = input("Enter number:")
	if userinp == 'done': break
	
	try:
		num = int(userinp)
		lst.append(num)
		
		#if smallest == None or num < smallest:
				#smallest = num
		#if largest == None or num > largest:
				#largest = num
				
	except:
		print("Invalid input")
		continue
		
print("Maximum is", max(lst))
print("Minimum is", min(lst))


