class Solution(object):
	def removeElement(self, nums, val):
		length = len(nums)
		count = 0
		for i in xrange(length):
			if nums[i] != val:
				nums[count] = nums[i]
				count += 1
		return count

if __name__ == "__main__":
	result = Solution().removeElement([3,2,2,3],3)
	print result
