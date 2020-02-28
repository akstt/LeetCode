class Solution:
    # 时间复杂度O(n)
    def maxSubArray1(self, nums: [int]) -> int:
        result = nums[0]
        num_temp = nums[0]
        for i in range(1, len(nums)):
            if num_temp > 0:
                num_temp += nums[i]
            else:
                num_temp = nums[i]
            result = max(result , num_temp)
        return result

    # 分治法
    def maxSubArray2(self, nums: [int]) -> int:

        def get_sum(index_start, index_middle, index_end):
            max_left = nums[index_middle]
            sum_left = nums[index_middle]
            for i in range(index_middle-1, index_start-1, -1):
                sum_left += nums[i]
                max_left = max(max_left, sum_left)
            max_right = nums[index_middle+1]
            sum_right = nums[index_middle+1]
            for i in range(index_middle+2, index_end + 1):
                sum_right += nums[i]
                max_right = max(sum_right, max_right)
            return max_right + max_left

        def max_subarray(index_start, index_end):
            if index_start == index_end:
                return nums[index_start]
            else:
                index_middle = (index_start + index_end)//2
                max_left = max_subarray(index_start, index_middle)
                max_right = max_subarray(index_middle + 1, index_end)
                max_all = get_sum(index_start, index_middle, index_end)
                return max(max_left, max_right, max_all)

        return max_subarray(0, len(nums) - 1)


if __name__ == "__main__":
    print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))