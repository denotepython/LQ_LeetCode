class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        for i in range(m):
            nums1.append(nums2[i])
        nums1.sort()
        if(n+m) % 2 == 0:
            mid = float(nums1[(n+m)/2-1] + nums1[(n+m)/2]) / 2
        else:
            mid = float(nums1[(n+m+1)/2-1])
        return mid

a = Solution()
nums1 = [1,2,3]
nums2 = [3,4]
ans = a.findMedianSortedArrays(nums1, nums2)
print ans
