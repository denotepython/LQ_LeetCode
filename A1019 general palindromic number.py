def is_palindromic(temp):
	length = len(temp)
	for i in range(0, length / 2):
		if(temp[i] != temp[length - 1 - i]): return False
	return True

num, radix = map(int, raw_input().split())
temp = []
if num == 0:
	print "Yes"
	print 0
else:
	while num != 0:
		temp.append(num%radix)
		num /= radix
	length = len(temp)

	condition = is_palindromic(temp)

	if condition == True:
		print "Yes"
	else:
		print "No"
	for i in range(length - 1, -1, -1):
		print temp[i],

#对于num=0的case没有考虑到，开始漏了3分