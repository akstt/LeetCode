class Solution:

    # 和上题思路类似
    # 由于是找最接近的数，所以利用字典的第一个方法就不适用了。采用第二个方法：先排序，再寻找
    # 时间复杂度O(n^2)
    # 空间复杂度O(n),存储排序后列表
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums = sorted(nums)
        # 三数之和
        result = sum(nums[:3])
        # 与target的接近程度
        result_sub = abs(result - target)
        for index_1, num_1 in enumerate(nums):
            # 双向查找
            index_2 = index_1 + 1
            index_3 = len(nums) - 1
            while index_2 < index_3:
                result_temp = num_1 + nums[index_2] + nums[index_3]
                result_sub_temp = abs(result_temp - target)
                if result_sub_temp < result_sub:
                    result, result_sub = result_temp, result_sub_temp
                if result_temp < target:
                    index_2 += 1
                elif result_temp > target:
                    index_3 -= 1
                else:
                    return result
        return result


if __name__ == "__main__":
    nums = [0, 1, 2]
    print(Solution().threeSumClosest(nums, 3))