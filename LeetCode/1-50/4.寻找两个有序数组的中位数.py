class Solution:

    # 暴力破解的时间复杂度O((m+n)/2),空间复杂度为O(1)
    # 题目要求时间复杂度为O(log(m + n))，使用二分法
    # 二分法寻找较短列表中中位数的位置，时间复杂度应该为O(log(min(m, n)))
    # 空间复杂度O(1)
    def findMedianSortedArrays_1(self, nums1: [int], nums2: [int]) -> float:
        # nums1为两个列表中较短的
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len_sum = len(nums1) + len(nums2)
        index_middle, flag = (len_sum - 1) // 2, (len_sum - 1) % 2
        # 两个列表都不为空
        if nums1 and nums2:
            start_index, end_index = 0, len(nums1) - 1
            index_1 = (start_index + end_index) // 2
            index_2 = index_middle - index_1
            # 添加哨兵，好处是当索引在边界处时可以不用做判断，坏处是修改了输入列表
            num_max = max(nums1[-1], nums2[-1]) + 1
            num_min = min(nums1[0], nums2[0]) - 1
            nums1.append(num_max)
            nums1.append(num_min)
            nums2.append(num_max)
            nums2.append(num_min)
            # 二分查找
            # 当循环不满足条件时，nums1[index_1], nums2[index_2]把nums1， nums2的分为两个部分，
            # 左边全部小于max(nums1[index_1], nums2[index_2]), 右边全部大于max(nums1[index_1], nums2[index_2])
            while max(nums1[index_1], nums2[index_2]) > min(nums1[index_1 + 1], nums2[index_2 + 1]):
                if nums1[index_1] > nums2[index_2]:
                    end_index = index_1 - 1
                else:
                    start_index = index_1 + 1
                index_1 = (start_index + end_index) // 2
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
            if flag:
                return (nums2[index_middle] + nums2[index_middle + 1]) / 2
            else:
                return nums2[index_middle]

    # 这个方法利用python的内置函数,
    # 时间复杂度为sort的时间复杂度为O((m+n)log(m+n))，
    # 存储新建的列表，空间复杂度为O（m+n）
    def findMedianSortedArrays_2(self, nums1, nums2) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        index_middle, flag = (len(nums3) - 1) // 2, (len(nums3) - 1) % 2
        if flag:
            return (nums3[index_middle] + nums3[index_middle + 1]) / 2
        else:
            return nums3[index_middle]

    # 和第一个算法想法一样，没用哨兵，在边界处要做判断
    # 参考别人代码写的，我感觉写的很好，假定列表末尾有一个绝对大的值，比较方便理解
    def findMedianSortedArrays_3(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        imin, imax, half_len = 0, len(nums1), (len(nums1) + len(nums2) + 1) // 2
        while True:
            i = (imin + imax) // 2
            j = half_len - i
            # 和第一个算法二分法想法差不多,目标max(nums1[i - 1], nums2[j - 1]) < min(nums1[i], nums2[j])，多了边界判断，
            if i < len(nums1) and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                # 中位数是max(nums1[i - 1], nums2[j - 1])或
                # (max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max_of_left
                if i == len(nums1):
                    min_of_right = nums2[j]
                elif j == len(nums2):
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0


if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    print(Solution().findMedianSortedArrays_3(nums1, nums2))
