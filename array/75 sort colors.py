class Solution(object):
    def sortColors(self, nums):
        temp = sorted(nums)
        for i in range(len(temp)):
            nums[i] = temp[i]