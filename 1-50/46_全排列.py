class Solution:

    # 传入数字，依次放在第一位，将剩下的数字放到下次递归当中
    def permute(self, nums: [int]) -> [[int]]:
        result_1 = []
        for num in nums:
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
    x = [1, 2, 3]
    print(Solution().permute(x))
