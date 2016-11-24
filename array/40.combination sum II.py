class Solution(object):
	def combinationSum2(self, candidates, target):
		length = len(candidates)
		cand = sorted(candidates)
		ans = []
		for i in xrange(length):
			temp_sum = cand[i]
			temp_ans = []
			if temp_sum > target:
				break
			elif temp_sum < target:
				temp_ans.append(cand[i])
			j = i + 1
			while j < length:
				temp_sum += cand[j]
				if temp_sum > target:
					j += 1
					break
				elif temp_sum < target:
					temp_ans.append(cand[j])
					j += 1 #错误在于这是累计求和了
				else:
					temp_ans.append(cand[j])
					ans.append(temp_ans)
					j = i + 1
		return ans

if __name__ == "__main__":
	result = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5],8)
	print result