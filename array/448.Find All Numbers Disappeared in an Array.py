class Solution(object):
	def findDisappearedNumbers(self, nums):
		length = len(nums)
		for i in xrange(length):
			if nums[abs(nums[i])-1] > 0:
				nums[abs(nums[i])-1] *= -1
		ans = []
		for i in xrange(length):
			if nums[i] > 0:
				ans.append(i+1)
		return ans

if __name__ == "__main__":
	result = Solution().findDisappearedNumbers([4,3,2,8,2,3,7,7])
	print result

