class Solution(object):
	def search(self, nums, target):
		length = len(nums)
		flag = False
		for i in xrange(length):
			if nums[i] == target:
				flag = True
				return i
				break
		if flag == False:
			return -1

if __name__ == "__main__":
	result = Solution().search([1,2,3,4,-2,-1],-1)
	print result

#确定没在逗我？遍历一次就结束，还hard？