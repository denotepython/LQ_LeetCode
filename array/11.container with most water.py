class Solution(object):
    def maxArea(self, height):
    	# MAX = 0
    	# length = len(height)
    	# for i in range(length):
    	# 	for j in range(i + 1, length):
    	# 		temp = (j - i) * min(height[i], height[j])
    	# 		if(temp > MAX):
    	# 			MAX = temp
    	# return MAX
        #暴力法可以通过41个case   
        length = len(height)
        i = 0
        j = length - 1
        MAX = (j - i) * min(height[i], height[j])
        while(i < j):
            if(height[i] < height[j]):
                i += 1
                temp = (j - i) * min(height[i], height[j])
                if(temp > MAX):
                    MAX = temp
            else:
                j -= 1
                temp = (j - i) * min(height[i], height[j])
                if(temp > MAX):
                    MAX = temp
        return MAX


a = Solution()
height = [1,2,3]
ans = a.maxArea(height)
print ans
