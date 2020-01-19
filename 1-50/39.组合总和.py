class Solution:

    # 递归解决
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        result = self.add_to_target(candidates, target, 0)
        return result

    # 递归部分
    # target：该递归需要得到的数
    # index_start：candidates的起始索引，不需要访问前面的数字（防止重复），
    def add_to_target(self, candidates, target, index_start):
        result_all = []
        # 依次添加数字
        for index_1 in range(index_start, len(candidates)):
            num_temp = candidates[index_1]
            # 得到答案
            if target == num_temp:
                result_all.append([num_temp])
                break
            # 进入下次递归，修改target和index_start
            elif target > num_temp:
                result_temp = self.add_to_target(candidates, target - num_temp, index_1)
                for result_ in result_temp:
                    result_.append(num_temp)
                    result_all.append(result_)
            # 列表已经排序，所以target < num_temp时，后面的数字不可能得到结果
            else:
                break
        return result_all


if __name__ == "__main__":
    candidates = [1, 2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
