"""
@Author: AKSTT
@Problem:
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
"""


# 暴力求解，时间复杂度O((m+n)/2),空间复杂度为O(1)
def findMedianSortedArrays_1(nums1, nums2) -> float:
    len_sum = len(nums1) + len(nums2)
    # flag表示中位数是否需要求平均
    index_middle, flag = (len_sum - 1)//2, (len_sum - 1) % 2
    # 哨兵：增加一个最大值放在每一个列表的末尾，可以少一些判断操作
    try:
        num_max = max(nums1[-1], nums2[-1]) + 1
    #  注释的一部分代表当有一个列表为空时，可以直接取非空列表的中位数
    except IndexError:
        if nums1:
            num_max = nums1[-1] + 1
            # nums3 = nums1
        else:
            num_max = nums2[-1] + 1
        #     nums3 = nums2
        # if flag:
        #     return (nums3[index_middle] + nums3[index_middle + 1])/2
        # else:
        #     return nums3[index_middle]
    nums1.append(num_max)
    nums2.append(num_max)
    i, j = 0, 0
    while i + j < index_middle:
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    if flag:
        if nums1[i] < nums2[j]:
            return (nums1[i] + min(nums1[i+1], nums2[j]))/2
        else:
            return (nums2[j] + min(nums2[j+1], nums1[i]))/2
    else:
        return min(nums1[i], nums2[j])


# 题目要求时间复杂度为O(log(m + n))
# 要求时间复杂度为log的，可以想到使用二分查找的方法
# 下面算法的时间复杂度应该为O（min(m, n)）
def findMedianSortedArrays_2(nums1, nums2) -> float:
    len_sum = len(nums1) + len(nums2)
    index_middle, flag = (len_sum - 1) // 2, (len_sum - 1) % 2
    # 两个列表都不为空
    if nums1 and nums2:
        # nums1为两个列表中较短的，
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        start_index, end_index = 0, len(nums1) - 1
        index_1 = (start_index + end_index)//2
        index_2 = index_middle - index_1
        # 哨兵
        num_max = max(nums1[-1], nums2[-1]) + 1
        num_min = min(nums1[0], nums2[0]) - 1
        nums1.append(num_max)
        nums1.append(num_min)
        nums2.append(num_max)
        nums2.append(num_min)
        # 二分查找
        # 当循环不满足条件时，nums1[index_1], nums2[index_2]把nums1， nums2的分为两个部分，
        # 左边全部小于max(nums1[index_1], nums2[index_2]), 右边全部大于max(nums1[index_1], nums2[index_2])
        # 或者是start_index > end_index
        # while start_index <= end_index:
        while max(nums1[index_1], nums2[index_2]) > min(nums1[index_1 + 1], nums2[index_2 + 1]):
            if nums1[index_1] > nums2[index_2]:
                end_index = index_1 - 1
            else:
                start_index = index_1 + 1
            index_1 = (start_index + end_index)//2
            index_2 = index_middle - index_1
        # 结果分析
        if nums1[index_1] < nums2[index_2]:
            # 中位数在nums1[index_1], nums1[index_1+1], nums2[index_2-1], nums2[index_2]中
            if flag:
                return (max(nums1[index_1], nums2[index_2 - 1]) + min(nums1[index_1 + 1], nums2[index_2])) / 2
            else:
                return max(nums1[index_1], nums2[index_2 - 1])
        else:
            if flag:
                return (max(nums2[index_2], nums1[index_1 - 1]) + min(nums2[index_2 + 1], nums1[index_1])) / 2
            else:
                return max(nums1[index_1 - 1], nums2[index_2])
    # 解决有列表为空的情况：
    else:
        if nums1:
            nums3 = nums1
        else:
            nums3 = nums2
        if flag:
            return (nums3[index_middle] + nums3[index_middle + 1])/2
        else:
            return nums3[index_middle]


# 这个方法利用python的内置函数,
# 时间复杂度为sort的时间复杂度为O((m+n)log(m+n))，空间复杂度为O（m+n）
# 虽然时间复杂度变高，但是由于sort为python内置函数，实际运行速度变快
def findMedianSortedArrays_3(nums1, nums2) -> float:
    nums3 = nums1 + nums2
    nums3.sort()
    index_middle, flag = (len(nums3) - 1) // 2, (len(nums3) - 1) % 2
    if flag:
        return (nums3[index_middle] + nums3[index_middle + 1])/2
    else:
        return nums3[index_middle]


if __name__ == "__main__":
    nums1 = [1, 2, 7]
    nums2 = [3, 6]
    print(findMedianSortedArrays_2(nums1, nums2))
