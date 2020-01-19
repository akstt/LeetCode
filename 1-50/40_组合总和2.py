class Solution:

    # 思路和上题差不多
    # 递归解决
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        result = self.add_to_target(candidates, target, 0)
        return result

    # 递归部分
    # target：该递归需要得到的数
    # index_start：candidates的起始索引，不需要访问前面的数字（防止重复），
    def add_to_target(self, candidates, target, index_start):
        result = []
        # num_use用来记录循环中上次循环使用的数字，如果新进来的数字和上次数字一样，则可以跳过这个数字
        num_use = candidates[0] - 1
        for index_1 in range(index_start, len(candidates)):
            num_temp = candidates[index_1]
            if num_temp == num_use:
                continue
            else:
                num_use = num_temp
            if num_temp == target:
                result.append([num_temp])
            elif target > num_temp:
                # index_start = index_1+1 防止一个数字多次使用
                result_temp = self.add_to_target(candidates, target-num_temp, index_1+1)
                for result_ in result_temp:
                    result_.append(num_temp)
                    result.append(result_)
            else:
                break
        return result

if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
