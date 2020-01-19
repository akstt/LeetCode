class Solution:

    # 想让容量增加，要么增加高度，要么增加宽度
    # 首先让宽度最大，那么只能靠增加高度来扩大容量
    # 遍历一遍列表，时间复杂度为O(n)
    # 空间复杂度为O(1)
    def maxArea_1(self, height: [int]) -> int:
        # 容器的左边界l_index，容器的右边界r_index
        l_index, r_index = 0, len(height) - 1
        # 暂时高度height_temp
        # height_temp = min(height[l_index], height[r_index])
        # 最大容量 result_max
        result_max = 0
        while l_index < r_index:
            if height[l_index] < height[r_index]:
                height_temp = height[l_index]
                result_max = max(result_max, height_temp * (r_index - l_index))
                while l_index < r_index and height[l_index] <= height_temp:
                    l_index += 1
            else:
                height_temp = height[r_index]
                result_max = max(result_max, height_temp * (r_index - l_index))
                while l_index < r_index and height[r_index] <= height_temp:
                    r_index -= 1
        return result_max


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea_1(height))
