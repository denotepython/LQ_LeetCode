# class Solution(object):
# 	def firstMissingPositive(self, nums):
# 		a = 99999999
# 		for i in xrange(len(nums)):
# 			if nums[i] > 999999:
# 				nums[nums[i]-a-1] += a
# 			else:
# 				nums[nums[i]-1] += a
			
# 		for i in xrange(len(nums)):
# 			if nums[i] < 999999:
# 				return i + 1
# 不对
# 终究思想是要让数组有两个作用，一是标记，但是同时不能破坏原有的信息
'''
class Solution(object):
	def firstMissingPositive(self, nums):
		n = len(nums)
		if n == 0:
			return 1
		s1 = n * (n+1) / 2
		s2 = 0
		for i in xrange(n):
			if nums[i] > 0:
				s2 += nums[i]
		ans = s1 - s2
		return ans
#求和的方法也不对，并不是一定是1-n,然后缺一个
'''
# class Solution(object):
# 	def firstMissingPositive(self, nums):
# 		i = 0
# 		while i < len(nums):
# 			if nums[i] > 0 and nums[i] != nums[nums[i]-1]:
# 				nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
# 			else:
class Solution:
    def firstMissingPositive(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] - 1 < len(nums) and nums[i] != nums[nums[i]-1]:
                #同一个i可以执行多次调换!!!
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        #使用python的enumerate获取索引和索引内容
        for i, integer in enumerate(nums):
            if integer != i + 1:
                return i + 1
        return len(nums) + 1				

if __name__ == "__main__":
	result = Solution().firstMissingPositive([3,4,-1,1])
	print result

