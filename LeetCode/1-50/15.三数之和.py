class Solution:

    # 思路仿照第一题两数之和
    # 先将所有两个不同的数加起来,保存结果
    # 然后逐个寻找可以相加为0的两个不同的数
    # 时间复杂度O(n^2)
    # 空间复杂度O(n)
    def threeSum_1(self, nums: [int]) -> [[int]]:
        # set 可以去重
        result = set()
        two_num_sum = {}
        # 先将所有两数相加的和保存起来
        for index_1, num_1 in enumerate(nums):
            for index_2, num_2 in enumerate(nums[index_1 + 1:], index_1+1):
                num_sum = num_1 + num_2
                two_num_sum.setdefault(-num_sum, []).append((index_1, index_2))
        # 依次寻找可以对应的两个数
        for index_1, num_1 in enumerate(nums):
            if num_1 in two_num_sum.keys():
                for index_two_num in two_num_sum[num_1]:
                    if index_1 not in index_two_num:
                        result_1 = [nums[index_1], nums[index_two_num[0]],
                        nums[index_two_num[1]]]
                        result_1.sort()
                        result.add(tuple(result_1))
        # 结果转成目标格式
        result = [list(result_) for result_ in result]
        return result

    # 先排序，再寻找
    # 时间复杂度O(n^2)
    # 空间复杂度O(n)
    def threeSum_2(self, nums: [int]) -> [[int]]:
        # 如果对原数组排序，空间复杂度为O（1）
        # 修改原数组不符合函数式编程思想
        nums = sorted(nums)
        result = set()
        # 注释的代码是另一种去重方法,就是答案的第一个数字，第二个数字不能和前一次一样
        # result = []
        # num_temp_1 = None

        for index_1, num_1 in enumerate(nums):

            # 后续相加永不可能为0
            if num_1 > 0:
                break
            # num_temp_2 = None
            # if num_1 == num_temp_1:
            #     continue
            # else:
            #     num_temp_1 = num_1
            # 第二个数和第三个数选择后面数字的第一个和最后一个，双向查找
            index_2 = index_1 + 1
            index_3 = len(nums) - 1
            while index_2 < index_3:
                # if nums[index_2] == num_temp_2:
                #     index_2 += 1
                #     continue
                num_sum = num_1 + nums[index_2] + nums[index_3]
                if num_sum > 0:
                    index_3 -= 1
                elif num_sum < 0:
                    index_2 += 1
                else:
                    result.add((num_1, nums[index_2], nums[index_3]))
                    # result.append([num_1, nums[index_2], nums[index_3]])
                    # num_temp_2 = num_temp_1[index_2]
                    index_2 += 1
                    index_3 -= 1
        # 结果转成目标格式
        result = [list(result_) for result_ in result]
        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum_1(nums))