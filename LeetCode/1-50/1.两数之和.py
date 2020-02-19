class Solution:

    # 建立字典，保存循环中迭代数字的索引，以及所需要的配对数字
    # python中字典是hash表，查找时间复杂度为O(1)，所以时间复杂度为O(n)
    # 需要新建字典，所以空间复杂度为O(n)
    def twoSum_1(self, nums: [int], target: int) -> [int]:
        # nums_index保存每次迭代中num的所需要配对数字的信息
        # key：target-num；value:num.index
        nums_index = {}
        for index_1 in range(len(nums)):
            nums_1 = nums[index_1]
            # 如果数字在nums_index的keys中，得到答案
            if nums_1 in nums_index.keys():
                index_2 = nums_index[nums_1]
                return [index_2, index_1]
            # 数字不在nums_index的keys中，保存所需信息
            else:
                nums_2 = target - nums_1
                nums_index[nums_2] = index_1

    # 同样的算法，python适合的写法
    def twoSum_2(self, nums: [int], target: int) -> [int]:
        nums_index = {}
        for index_1, num_1 in enumerate(nums):
            try:
                return [nums_index[num_1], index_1]
            except KeyError:
                nums_index[target-num_1] = index_1


# 测试
if __name__ == "__main__":
    nums = [5, 3, 3]
    target = 6
    print(Solution().twoSum_2(nums, target))
