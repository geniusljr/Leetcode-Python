class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        intervals.sort(lambda x,y:cmp(x.start, y.start) if x.start != y.start else cmp(x.end, y.end))
        result = []
        if (len(intervals) == 0):
            return result
        last = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start <= last.end and intervals[i].end > last.end:
                last.end = intervals[i].end
            elif intervals[i].start > last.end:
                result.append(last)
                last = Interval(intervals[i].start, intervals[i].end)
        result.append(last)
        return result
