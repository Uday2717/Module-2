l = ["john","abrahim","vicky","vin","roman"]
 
print("The original list : " + str(l))

max_len = 1
for i in l:
	if len(i) > max_len:
		max_len = len(i)
		result = i
		
print("Maximum length string is : " + result)
