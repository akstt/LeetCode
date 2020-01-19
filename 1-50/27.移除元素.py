class Solution:

    # 和上题思路类似，index_1指向数值为val的元素，index_2遍历列表
    # 时间复杂度O(n)
    # 空间复杂度O(1)
    def removeElement(self, nums: [int], val: int) -> int:
        index_1 = 0
        for index_2, num in enumerate(nums):
            if num != val:
                nums[index_1], nums[index_2] = nums[index_2], nums[index_1]
                index_1 += 1
        return index_1


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(Solution().removeElement(nums, val), nums)
