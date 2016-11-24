# class Solution(object):
# 	def searchInsert(self, nums, target):
# 		i = 0
# 		while i < len(nums):
# 			if i == len(nums) - 1 and nums[i] < target:
# 				return len(nums)
# 			else:
# 				if nums[i] < target:
# 					i += 1
# 				else:
# 					return i
#O(n)
class Solution(object):
	def searchInsert(self, nums, target):
		i, j = 0, len(nums)-1
		while i <= j: #若是i < j的条件，长为1的不会进入这个循环
			if j == len(nums) - 1 and nums[j] < target:
				return len(nums)
			else:
				mid = (i + j) / 2
				if nums[mid] < target:
					i += 1
				elif nums[mid] > target:
					j -= 1
				else:
					return mid
		if i > j:
			return i
#复杂度O(log(n))，提高了50%

if __name__ == "__main__":
	result = Solution().searchInsert([1,3,5,6], 0)
	print result
	
