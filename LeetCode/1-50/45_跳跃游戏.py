import math


class Solution:

    # 动态规划
    def jump_1(self, nums: [int]) -> int:
        result = [0] * len(nums)
        for index_1 in range(len(nums)-2,-1,-1):
            one_step_scope = nums[index_1]
            if one_step_scope == 0:
                result[index_1] = len(nums)
                continue
            step_min = 1+result[index_1 + 1]

            if int(step_min) != step_min:
                step_min += 1
            # step_min = math.ceil((len(nums) - index_1 - 1) / one_step_scope)
            for index_2 in range(index_1 + 1, index_1 + one_step_scope + 1, 1):
                if index_2 < len(nums):
                    step_temp = 1 + result[index_2]
                    step_min = min(step_min, step_temp)
                else:
                    break
            result[index_1] = step_min
        return int(result[0])

    # 贪心算法
    def jump_2(self, nums: [int]) -> int:
        step_num = 0
        step_max = 0
        step_max_temp = 0
        for index_1 in range(len(nums)-1):
            step_max_temp = max(step_max_temp, index_1 + nums[index_1])
            if index_1 == step_max:
                step_max = step_max_temp
                step_num += 1
        return step_num

if __name__ == "__main__":
    x = [2,3,1,1,4]
    print(Solution().jump_2(x))
