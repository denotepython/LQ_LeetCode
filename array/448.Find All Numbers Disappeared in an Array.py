class Solution(object):
	def findDisappearedNumbers(self, nums):
		length = len(nums)
		for i in xrange(length):
			if nums[abs(nums[i])-1] > 0:
				nums[abs(nums[i])-1] *= -1
		ans = []
		for i in xrange(length):
			if nums[i] > 0:
				ans.append(i+1)
		return ans

# class Solution:
#     def findDisappearedNumbers(self, nums):
#         i = 0
#         while i < len(nums):
#             if nums[i] > 0 and nums[i] - 1 < len(nums) and nums[i] != nums[nums[i]-1]:
#                 #同一个i可以执行多次调换!!!
#                 nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
#             else:
#                 i += 1
#         #使用python的enumerate获取索引和索引内容
#         ans = []
#         for i, integer in enumerate(nums):
#             if integer != i + 1:
#                 ans.append(i+1)
  
if __name__ == "__main__":
	result = Solution().findDisappearedNumbers([4,3,2,8,2,3,7,1])
	print result

