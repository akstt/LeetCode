class Solution:

    # 从后向前遍历列表，找到index_1,是第一个nums[index_1-1] < nums[index_1]，开始处理。
    # 基本想法是nums[index_1:]是能组成的最大数字，翻转该部，为最小数字，再进一位，增大nums[index_1-1],就可以达成目标
    # 如果没找到符合要求的数字索引位置，翻转列表
    # 时间复杂度O(n)
    # 空间复杂度O(1)
    def nextPermutation(self, nums: [int]) -> None:
        # index_1 nums[index_1:] 为倒序排列
        index_1 = 0
        for index_1 in range(len(nums)-1, 0, -1):
            if nums[index_1-1] < nums[index_1]:
                break
        # 没找到，翻转列表
        else:
            nums.reverse()
            return
        # 翻转nums[index_1: ], index_2，index_3翻转列表的两端
        index_2 = index_1
        index_3 = len(nums) - 1
        while index_2 < index_3:
            nums[index_2], nums[index_3] = nums[index_3], nums[index_2]
            index_2 += 1
            index_3 -= 1
        # 在nums[index_1: ]，找到比nums[index_1-1]稍大的数，完成进位
        for index_4 in range(index_1, len(nums)):
            if nums[index_4] > nums[index_1-1]:
                nums[index_1-1], nums[index_4] = nums[index_4], nums[index_1-1]
                break


if __name__ == "__main__":
    a = [1,2,3]
    Solution().nextPermutation(a)
    print(a)