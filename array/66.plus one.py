class Solution(object):
    def plusOne(self, digits):
        num = 0
        for i in digits[::]:
            num = num * 10 + i
        num += 1
        ans = []
        while num != 0:
            ans.append(num % 10)
            num /= 10
        ans.reverse()
        return ans
        """
        :type digits: List[int]
        :rtype: List[int]
        """

if __name__=="__main__":
    result = Solution().plusOne([1,4,5,9])
    print result
