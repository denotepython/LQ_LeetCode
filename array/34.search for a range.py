# -*- coding: utf-8 -*-
def findLeftIndex(left, right, nums, target):
	flag = False
	length = len(nums)
	if length == 1:
		if nums[0] == target:
			return 0
	while left < right:
		mid = (left + right) / 2
		if target == nums[mid]:
			right = mid
			flag = True
		else:
			left = mid + 1
	if flag == True:		
		return left
	else:
		return -1
 
def findRightIndex(left, right, nums, target):
	flag = False
	length = len(nums)
	if length == 1:
		if nums[0] == target:
			return 0
	while left < right:
		mid = (left + right) / 2
		if nums[mid] > target:
			right = mid
			flag == True
		else:
			left = mid + 1
	if flag == False:
		return left   #但是存在这样一种情况，所有的值都等于target
	else:
		return left - 1 #正常查找到第一个大于target的下标然后减1

class Solution(object):
	def searchRange(self, nums, target):
		length = len(nums)
		left = findLeftIndex(0, length-1, nums, target)
		right = findRightIndex(0, length-1, nums, target)
		if left == -1:
			ans = [-1,-1]
			return ans
		ans = [left, right]
		return ans

if __name__ == "__main__":
	result = Solution().searchRange([1,3],1)
	print result
