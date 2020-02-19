class Solution:
    # 要求时间复杂度O(n), 空间复杂度O(1)
    # 重点是空间复杂度的要求
    # 结果只可能是[1, len(nums)+1]中的一个正整数
    def firstMissingPositive_1(self, nums: [int]) -> int:
        if 1 not in nums:
            return 1
        # 遍历列表，把不在[1, len(nums))中的数替换为1
        for index_1, num in enumerate(nums):
            if num < 1 or num > len(nums):
                nums[index_1] = 1
        # 遍历列表，把nums[num-1]变为负数,这样，只要遍历一遍列表，找到第一个正数，那么结果就是该正数索引+1
        for num in nums:
            num = abs(num)
            nums[num - 1] = -abs(nums[num - 1])
        for index_1, num in enumerate(nums):
            if num > 0:
                return index_1 + 1
        return len(nums) + 1

    # 桶排序
    def firstMissingPositive_2(self, nums: [int]) -> int:
        # 将出现在[1, len(nums)]中的数字num放在索引为num-1的地方
        for index_1, num in enumerate(nums):
            while 0 < num <= len(nums) and nums[num-1] != num:
                nums[num-1], nums[index_1] = nums[index_1], nums[num-1]
                num = nums[index_1]
        # 如果num != index_1 + 1则缺失的数为index_1 + 1
        for index_1, num in enumerate(nums):
            if num != index_1 + 1:
                return index_1 + 1
        return len(nums) + 1


if __name__ == "__main__":
    print(Solution().firstMissingPositive_2([3, 4, -1, 1]))
