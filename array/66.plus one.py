class Solution(object):
    def plusOne(self, digits):
        length = len(digits)
        num = 0
        for i in xrange(length-1,-1):
            num += num * 10 + digits[i]
        num += 1
        ans = []
        while num != 0:
            ans.append(num/10)
        ans.reverse()
        return num
        """
        :type digits: List[int]
        :rtype: List[int]
        """

if __name__=="__main__":
    result = Solution().plusOne([1,4,5])
    print result
