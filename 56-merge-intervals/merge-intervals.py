class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        i = 0
        while i < len(intervals)-1:
                val1 = intervals[i][1]
                val2 = intervals[i+1][0]
                if val1 >= val2:
                    start = min(min(intervals[i]), min(intervals[i+1]))
                    end = max(max(intervals[i]), max(intervals[i+1]))
                    intervals[i] = [start,end]
                    intervals.pop(i+1)
                else:
                    i +=1   
        return intervals    