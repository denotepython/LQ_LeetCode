class Solution(object):
    def isPalindrome(self, x):
    	y = list()
    	count = 0
    	while x != 0:
    		mod = x % 10
    		y.append(mod)
    		x = x / 10
    		count += 1

        i = 0
        j = count - 1
        while i <= j:
        	if y[i] == y[j]:
        		i += 1
        		j -= 1
        	else:
        		return False
        return True

        """
        :type x: int
        :rtype: bool
        """
        

test = Solution()
print test.isPalindrome(12331)
