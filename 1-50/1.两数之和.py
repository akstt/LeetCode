"""
@Author: AKSTT
@Problem:
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# 暴力求解 时间复杂度O(n^2), 空间复杂度为O(1)
def twoSum_1(nums: [int], target: int) -> [int]:
    for index_1, num_1 in enumerate(nums):
        for index_2, num_2 in enumerate(nums[index_1+1:], index_1+1):
            if num_1 + num_2 == target:
                return [index_1, index_2]
    return None


# 第二个循环利用二分查找，时间复杂度为O(nlogn), 空间复杂度为O(1)
def twoSum_2(nums: [int], target: int) -> [int]:
    for index_1, num_1 in enumerate(nums):
        index_2_start, index_2_end = index_1, len(nums)
        # 二分查找确定第二个数
        while index_2_start < index_2_end - 1:
            index_2 = (index_2_start + index_2_end)//2
            num_sum = nums[index_2] + num_1
            if num_sum == target:
                return [index_1, index_2]
            elif num_sum < target:
                index_2_start = index_2
            else:
                index_2_end = index_2
    return None


# 实际上这个题目的输入是没有排序的,所以twoSum_2是无法通过测试的
# 下面的代码经过处理可以通过测试,不过新建了一个列表, 空间复杂度变为O(n),时间复杂度依然为O(nlogn)
def twoSum_3(nums: [int], target: int) -> [int]:
    # nums_sort为排序后数组
    nums_sorted = sorted(nums)
    for index_1, num_1 in enumerate(nums_sorted):
        index_2_start, index_2_end = index_1, len(nums_sorted)
        while index_2_start < index_2_end - 1:
            index_2 = (index_2_start + index_2_end) // 2
            num_2 = nums_sorted[index_2]
            num_sum = num_2 + num_1
            # 处理相同的整数的情况
            if num_sum == target:
                if num_1 == num_2:
                    index_1 = nums.index(num_1)
                    index_2 = nums.index(num_1, index_1 + 1)
                else:
                    index_1, index_2 = nums.index(num_1), nums.index(num_2)
                return [index_1, index_2]
            elif num_sum < target:
                index_2_start = index_2
            else:
                index_2_end = index_2
    return None


# 利用字典，保存循环中每次出现的结果
# python中字典是hash表，查找时间复杂度为O(1),所以会快很多
# 时间复杂度为O(n), 需要新建字典，所以空间复杂度为O(n)
def twoSum_4(nums: [int], target: int) -> [int]:
    index_nums = {}
    for index_2, num_1 in enumerate(nums):
        try:
            return [index_nums[num_1], index_2]
        except KeyError:
            index_nums[target-num_1] = index_2


if __name__ == "__main__":
    nums = [5, 3, 3]
    target = 6
    print(twoSum_4(nums, target))
