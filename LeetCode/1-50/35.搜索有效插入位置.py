class Solution:

    # 二分法解决
    # 时间复杂度O(logn)
    # 空间复杂度O(1)
    def searchInsert(self, nums: [int], target: int) -> int:
        index_start, index_end = 0, len(nums) - 1
        while index_start <= index_end:
            index_middle = (index_start + index_end) // 2
            if target < nums[index_middle]:
                index_end = index_middle - 1
            elif target > nums[index_middle]:
                index_start = index_middle + 1
            else:
                return index_middle
        return index_start


if __name__ == "__main__":
    nums, target = [1, 3, 5, 6], 7
    print(Solution().searchInsert(nums, target))
