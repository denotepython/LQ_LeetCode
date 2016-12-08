class Solution(object):
	def canJump(self, nums):
		if len(nums) == 1:
			flag = True
			return flag
		pre, now = 0, nums[0]
		while 1:
			if now >= len(nums) - 1:
				flag = True
				return flag
			if nums[now] != 0:
				pre = now
				now += nums[now]
			else:
				if nums[pre] == 0 :
					flag = False
					return flag
				else:
					pre += 1
					now = pre + nums[pre]
			
if __name__ == "__main__":
	result = Solution().canJump([3,0,8,2,0,0,1])
	print result

#上述代码问题在于每次默认选择了键值作为跳的步数
#其实跳的步数可以小于该键值
#[3,0,8,2,0,0,1]，第一次跳3步那么失败，但是选择跳2步就可以成功