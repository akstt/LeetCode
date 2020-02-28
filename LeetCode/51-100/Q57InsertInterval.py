class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if len(intervals) == 0:
            return [newInterval]
        result = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else:
                result.append([min(intervals[i][0], newInterval[0]), newInterval[1]])
                break
            i += 1
        else:
            if newInterval[0] <= result[-1][1]:
                result[-1][1] = max(intervals[-1][1], newInterval[1])
            else:
                result.append(newInterval)
            return result
        while i < len(intervals) and intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(intervals[i][1], result[-1][1])
            i += 1
        for j in range(i, len(intervals)):
            result.append(intervals[j])
        return result


def main():
    print(Solution().insert([[1, 5]], [0, 0]))


if __name__ == "__main__":
    main()
