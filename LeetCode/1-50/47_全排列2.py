class Solution:

    # 和上题想法一样，添加
    def permuteUnique(self, nums: [int]) -> [[int]]:
        # 排序，用于去重
        nums.sort()
        return self.permute(nums)

    # 除了添加下面if判断用于去重外,和46题的代码一样
    def permute(self, nums: [int]) -> [[int]]:
        result_1 = []
        num_last = nums[0] - 1
        for num in nums:
            # 去重
            if num == num_last:
                continue
            num_last = num
            nums_temp = nums.copy()
            nums_temp.remove(num)
            if len(nums_temp) > 0:
                # 将剩余数字的全排列并在num后面，组成全排列
                results_return = self.permute(nums_temp)
                for result_return in results_return:
                    result_add = [num]
                    result_add.extend(result_return)
                    result_1.append(result_add)
            else:
                result_1.append([num])
        return result_1


if __name__ == "__main__":
    x = [1,1,2]
    print(Solution().permuteUnique(x))