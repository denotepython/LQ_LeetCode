class Solution(object):
	def maxSubArray(self, nums):
		if max(nums) < 0:
			return max(nums)
		G_max, L_max = -1000000, 0
		for i in xrange(len(nums)):
			L_max = max(0, L_max+nums[i])
			G_max = max(G_max, L_max)
		return G_max

if __name__ == "__main__":
	result = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
	print result
