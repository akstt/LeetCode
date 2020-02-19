class Solution:

    # 时间复杂度O(n)
    # 空间复杂度O(1)
    # 把容器想象为上下叠放的容器，从下向上依次求容量，最后减去容器占的体积
    # 左右双指针，分别指向容器两边
    def trap(self, height: [int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        # 当前容器的底部高度
        temp_height = 0
        capacity = 0
        # 找到更高的杯子，依次容量相加
        while left_index <= right_index:
            if height[left_index] <= temp_height:
                left_index += 1
            elif height[right_index] <= temp_height:
                right_index -= 1
            else:
                new_height = min(height[left_index], height[right_index])
                capacity += (new_height - temp_height) * (right_index + 1 - left_index)
                temp_height = new_height
        return capacity - sum(height)


if __name__ == "__main__":
    x = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(x))
