class Solution:
    def canJump(self, nums: [int]) -> bool:
        index_1 = 0
        max_index = 0
        while index_1 <= max_index:
            if index_1 >= len(nums) - 1:
                return True
            max_index = max(max_index, nums[index_1] + index_1)
            index_1 += 1
        return False
