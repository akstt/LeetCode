class Solution:

    # 和15.三数之和想法类似，先排序，然后固定前两个数，再找后两个数
    # 时间复杂度O(n^3)
    # 空间复杂度O(n)
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        result = set()
        nums = sorted(nums)
        for index_1, num_1 in enumerate(nums):
            for index_2, num_2 in enumerate(nums[index_1+1:], index_1+1):
                # 固定前两个数字，双向寻找
                index_3 = index_2 + 1
                index_4 = len(nums) - 1
                while index_3 < index_4:
                    # 跳出判断，能得到的最小和和最大和不满足要求，跳出
                    num_min = num_1 + num_2 + nums[index_3] + nums[index_3+1]
                    num_max = num_1 + num_2 + nums[index_4-1] + nums[index_4]
                    if num_min > target or num_max < target:
                        break
                    num_sum = num_1 + num_2 + nums[index_3] + nums[index_4]
                    if num_sum > target:
                        index_4 -= 1
                    elif num_sum < target:
                        index_3 += 1
                    else:
                        result.add((num_1, num_2, nums[index_3], nums[index_4]))
                        index_3 += 1
                        index_4 -= 1
        # 结果转成目标格式
        result = [list(result_) for result_ in result]
        return result


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))