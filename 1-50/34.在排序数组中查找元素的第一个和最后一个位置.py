class Solution:

    # 题目要求时间复杂度O(logn)
    # 可以写递归，下面是循环版本
    def searchRange(self, nums: [int], target: int) -> [int]:
        result = [0, len(nums) - 1]
        index_middle = -1
        # 找到target最左索引
        index_start, index_end = result
        while index_start < index_end:
            index_middle = (index_start + index_end)//2
            if target > nums[index_middle]:
                index_start = index_middle + 1
            elif target < nums[index_middle]:
                index_end = index_middle - 1
            else:
                index_end = index_middle
        if not nums or nums[index_start] != target:
            return [-1, -1]
        result[0] = index_start
        # 找到target最右索引
        index_start, index_end = result
        while index_start < index_end:
            index_middle = (index_start + index_end + 1)//2
            if target > nums[index_middle]:
                index_start = index_middle + 1
            elif target < nums[index_middle]:
                index_end = index_middle - 1
            else:
                index_start = index_middle
        result[1] = index_end
        return result


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]

    target = 6
    print(Solution().searchRange(nums, target))