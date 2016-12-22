#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        length = len(Intervals)
        ans = Interval()
        count = 0
        while i < length-1:
            if intervals[i].e > intervals[i+1].s:
                ans[count].s = intervals[i].s
                ans[count].e = intervals[i+1].s
            else:
                count += 1
            i += 1
            

        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """