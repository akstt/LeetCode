class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: [x[0]])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result
