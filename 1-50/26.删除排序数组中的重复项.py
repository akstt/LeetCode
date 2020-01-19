class Solution:

    # 麻烦的是要求在原地进行修改
    # 双指针，index_1指向需要换的位置，index_2遍历列表寻找不重复元素
    # 时间复杂度O(n)
    # 空间复杂度O(1)
    def removeDuplicates(self, nums: [int]) -> int:
        index_1 = 0
        # num_temp寻找不重复元素
        num_temp = None
        for index_2, num in enumerate(nums):
            # 不重复时，把元素放到index_1位置
            if num != num_temp:
                nums[index_1] = num
                index_1 += 1
                num_temp = num
        return index_1


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
    index_all = Solution().removeDuplicates(nums)
    print(nums, index_all)
