class Solution(object):
	def trap(self, height):
		length = len(height)
		if length == 0:
			return 0
		i, j = 0, length-1
		left, right = height[i], height[j]
		water = 0
		while i < j:
			if left < right:
				i += 1
				water += max(0, left-height[i])
				left = max(left,height[i])
			else:
				j -= 1
				water += max(0, right-height[j])
				right = max(height[j],right)
		return water

if __name__ == "__main__":
	result = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
	print result
