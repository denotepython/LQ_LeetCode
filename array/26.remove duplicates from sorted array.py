class Solution(object):
	def removeDuplicates(self, nums):
		# s = set(nums)
		# nums = list(s)
		# length = len(nums)
		# return nums
		length = len(nums)
		if length == 0:
			return 0
		index,j = 0,1
		while j < length:
			if nums[j] != nums[index]:
				index += 1
				nums[index] = nums[j]
			j += 1
		len2 = index + 1
		return len2
		"""
		:type nums: List[int]
		:rtype: int
		"""
if __name__ == '__main__':
    result = Solution().removeDuplicates([1,1,2])
    print result

#懂了，不能开启新的空间，要改变原来的list
#不用处理剩下多余的元素，只要0-index-1是互不重复的元素
#用list(set())会超时