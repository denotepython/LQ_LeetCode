class Solution(object):
    def threeSum(self, nums):
        length = len(nums)
        nums = sorted(nums)
        ans = []

        i = 0
        while i < length:
            if(nums[i] != nums[i - 1] or i == 0):
                j, k = i + 1, length - 1
                while j < k:
                    if(nums[i] + nums[j] + nums[k] == 0):
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
                    elif(nums[i] + nums[j] + nums[k] > 0):
                        k -=1
                    else:
                        j += 1
            i += 1    
        return ans

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
a = Solution()
ans = a.threeSum(nums)
print ans

'''
1、比如[-2,-2,-2,-2,4]
首先，对于后面三个-2不需要在进行 遍历求解
if(nums[i] != nums[i - 1] or i == 0)
通过这一句处理初始状态

其次，对于第一个-2本身也会有重复的情况
[-1,-2,4]其中第二个-2可以是1、2、3、4位的-2也要处理这种重复的
while j < k and nums[j] == nums[j-1]:
    j += 1
while j < k and nums[k] == nums[k+1]:
    k -= 1
用这个去重

2、第一次处理三个变量的问题，本质上和O(n2)降到O(n)一样
通过双指针将O(n3)降为O(n2)