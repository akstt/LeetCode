class Solution:

    # 要求时间复杂度为O(logn),二分法解决
    # 二分查找的部分不在赘述
    # 可以把列表分为两部分
    def search(self, nums: [int], target: int) -> int:
        index_start, index_end = 0, len(nums) - 1
        if not nums:
            return -1
        # 结果在左半部分
        if target >= nums[0]:
            while index_start <= index_end:
                index_middle = (index_start + index_end) // 2
                num_temp = nums[index_middle]
                if num_temp == target:
                    return index_middle
                # 如果此时num_temp < nums[0] 则说明index_middle跑到右半部分去了
                elif num_temp > target or num_temp < nums[0]:
                    index_end = index_middle - 1
                else:
                    index_start = index_middle + 1
        # 结果在右半部分
        elif target <= nums[-1]:
            while index_start <= index_end:
                index_middle = (index_start + index_end) // 2
                num_temp = nums[index_middle]
                if num_temp == target:
                    return index_middle
                # 如果此时num_temp > nums[-1] 则说明index_middle跑到左半部分去了
                elif num_temp < target or num_temp > nums[-1]:
                    index_start = index_middle + 1
                else:
                    index_end = index_middle - 1
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))