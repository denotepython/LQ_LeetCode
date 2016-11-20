class Solution(object):
	def fourSum(self, nums, target):
		length = len(nums)
		ans = []
		nums = sorted(nums)
		if length < 4:
			return ans
		count = 0
		for i in xrange(length):
			if nums[i] == 0:
				count += 1
			else:
				break
		if count == length and target == 0:
			ans.append([0,0,0,0])
			return ans

		for i in xrange(0,length - 3):
			if i == 0 or nums[i] != nums[i-1]:
				for j in xrange(i + 1,length - 2):
					if j != i + 1 and nums[j] == nums[j-1]: #这一个条件肯定不对，[-1, -1, 0, 1]=-1的情况会漏
						continue 						#但是不加这一句又有的重复解没有排除
					p, q = j + 1, length - 1        
					while p < q:
						diff = nums[i] + nums[j] + nums[p] + nums[q] - target
						if diff < 0:
							p += 1
						elif diff > 0:
							q -= 1
						else:
							ans.append([nums[i], nums[j], nums[p], nums[q]])
							p += 1
							q -= 1
							while p < q and nums[p] == nums[p + 1]: #必须加上p<q,否则可能会超过
								p += 1
							while p < q and nums[q] == nums[q - 1]:
								q -= 1						
					j += 1
			i += 1
		return ans

if __name__ == '__main__':
    result = Solution().fourSum([-1,0,1,2,-1,-4], -1)
    print result

#[1,0,-1,0,-2,2]
#0