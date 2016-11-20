class Solution(object):
	def threeSumClosest(self, nums, target):
		length = len(nums)
		ans = []
		nums = sorted(nums)
		closet = 10000000
		for i in xrange(length-2):
			if i == 0 or nums[i] != nums[i-1]:
				j, k = i + 1, length - 1
				while j < k:
					diff = nums[i] + nums[j] + nums[k] - target#这一句位置在while循环内
					if abs(diff) < closet:
						closet = abs(diff)
						ans = nums[i] + nums[j] + nums[k]
					if diff < 0 :
						j += 1
					elif diff > 0:
						k -= 1
					else:
						print nums[i], nums[j], nums[k],
						j += 1
						k -= 1
		return ans
nums = [0, 2, 1, -3]
target = 1
a = Solution()
ans = a.threeSumClosest(nums, target)
print ans 
