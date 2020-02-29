# 冒泡排序
def bubble_sort(list_insert):
    """
    时间复杂度：最好情况O(N),最坏情况O(n^2)
    稳定
    :param list_insert: 需要排序的列表，原地修改
    """
    for index_last in range(len(list_insert)-1, -1, -1):
        flag = True
        for index_1 in range(index_last):
            if list_insert[index_1 + 1] < list_insert[index_1]:
                list_insert[index_1], list_insert[index_1+1] = list_insert[index_1+1], list_insert[index_1]
                flag = False
        if flag:
            break


# 插入排序
def insertion_sort(list_insert):
    """
    时间复杂度：最好情况O(N),最坏情况O(n^2)
    稳定
    :param list_insert: 需要排序的列表，原地修改
    """
    for index_sort in range(1, len(list_insert)):
        num_temp = list_insert[index_sort]
        i = index_sort
        while i > 0:
            if list_insert[i-1] > num_temp:
                list_insert[i] = list_insert[i-1]
                i -= 1
            else:
                break
        list_insert[i] = num_temp


# 希尔排序
def shell_sort(list_insert):
    """
    时间复杂度：最坏情况O(n^2)(和增量序列有关)
    :param list_insert: 需要排序的列表，原地修改
    """
    distance = len(list_insert)//2
    while distance > 0:
        for index_1 in range(distance, len(list_insert)):
            num_temp = list_insert[index_1]
            index_2 = index_1
            while index_2 >= distance:
                if list_insert[index_2-distance] > num_temp:
                    list_insert[index_2] = list_insert[index_2-distance]
                    index_2 -= distance
                else:
                    break
            list_insert[index_2] = num_temp
        distance = distance // 2


# 选择排序
def selection_sort(list_insert):
    """"
    时间复杂度：O(n ^ 2)
    :param list_insert: 需要排序的列表，原地修改
    """
    for index_1 in range(len(list_insert)):
        index_min_value = index_1
        for index_2 in range(index_1+1, len(list_insert)):
            if list_insert[index_2] < list_insert[index_min_value]:
                index_min_value = index_2
        list_insert[index_1], list_insert[index_min_value] = list_insert[index_min_value], list_insert[index_1]


# 堆排序
def heap_sort(list_insert):
    """"
    时间复杂度：O(n*log(n))
    :param list_insert: 需要排序的列表，原地修改
    """
    # 建立最大堆
    def build_heap(list_to_build, index_start, index_end):
        index_left = index_start * 2 + 1
        index_right = index_start * 2 + 2
        if index_left == index_end:
            if list_to_build[index_left] > list_to_build[index_start]:
                list_to_build[index_start], list_to_build[index_left] = \
                    list_to_build[index_left], list_to_build[index_start]
        elif index_right <= index_end:
            if max(list_to_build[index_left], list_to_build[index_right]) > list_to_build[index_start]:
                if list_to_build[index_left] > list_to_build[index_right]:
                    list_to_build[index_start], list_to_build[index_left] = \
                        list_to_build[index_left], list_to_build[index_start]
                    build_heap(list_to_build, index_left, index_end)
                else:
                    list_to_build[index_start], list_to_build[index_right] = \
                        list_to_build[index_right], list_to_build[index_start]
                    build_heap(list_to_build, index_right, index_end)

    for i in range(len(list_insert)//2, -1, -1):
        build_heap(list_insert, i, len(list_insert)-1)

    for i in range(len(list_insert)-1, 0, -1):
        list_insert[0], list_insert[i] = list_insert[i], list_insert[0]
        build_heap(list_insert, 0, i-1)


# 归并排序
def merge_sort(list_insert):
    """"
    时间复杂度：O(n*log(n))
    稳定
    :param list_insert: 需要排序的列表，原地修改
    """
    # 治
    def merge(list_to_sort, list_to_store, index_start_1, index_end_1, index_end_2):
        index_start_2 = index_end_1 + 1
        index_store = index_start_1
        index_start = index_store
        while index_start_1 <= index_end_1 and index_start_2 <= index_end_2:
            if list_to_sort[index_start_1] <= list_to_sort[index_start_2]:
                list_to_store[index_store] = list_to_sort[index_start_1]
                index_start_1 += 1
            else:
                list_to_store[index_store] = list_to_sort[index_start_2]
                index_start_2 += 1
            index_store += 1
        while index_start_1 <= index_end_1:
            list_to_store[index_store] = list_to_sort[index_start_1]
            index_start_1 += 1
            index_store += 1
        while index_start_2 <= index_end_2:
            list_to_store[index_store] = list_to_sort[index_start_2]
            index_start_2 += 1
            index_store += 1
        for index_1 in range(index_start, index_store):
            list_to_sort[index_1] = list_to_store[index_1]

    # 分
    def divide(list_to_sort, list_to_store, index_start, index_end):
        if index_start < index_end:
            index_middle = (index_start + index_end) // 2
            divide(list_to_sort, list_to_store, index_start, index_middle)
            divide(list_to_sort, list_to_store, index_middle + 1, index_end)
            merge(list_to_sort, list_to_store, index_start, index_middle, index_end)

    # list_temp = [None] * len(list_insert)
    # divide(list_insert, list_temp, 0, len(list_insert)-1)

    # 归并排序循环
    def merge_sort_length(list_to_sort, list_to_store, length):
        index_start = 0
        while index_start <= len(list_to_sort) - 2 * length:
            merge(list_to_sort, list_to_store, index_start, index_start + length - 1, index_start + 2 * length - 1)
            index_start += 2 * length
        if len(list_to_sort) - index_start > length:
            merge(list_to_sort, list_to_store, index_start, index_start + length - 1, len(list_to_sort)-1)

    merge_length = 1
    list_temp = [None] * len(list_insert)
    while merge_length < len(list_insert):
        merge_sort_length(list_insert, list_temp, merge_length)
        merge_length *= 2


# 快速排序
def quick_sort(list_insert):
    """"
    时间复杂度：O(n*log(n))
    :param list_insert: 需要排序的列表，原地修改
    """
    # 选取主元
    def get_pivot(index_start, index_end):
        index_middle = (index_start + index_end)//2
        if list_insert[index_start] > list_insert[index_middle]:
            list_insert[index_start], list_insert[index_middle] = list_insert[index_middle], list_insert[index_start]
        if list_insert[index_start] > list_insert[index_end]:
            list_insert[index_start], list_insert[index_end] = list_insert[index_end], list_insert[index_start]
        if list_insert[index_middle] > list_insert[index_end]:
            list_insert[index_middle], list_insert[index_end] = list_insert[index_end], list_insert[index_middle]
        list_insert[index_end-1], list_insert[index_middle] = list_insert[index_middle], list_insert[index_end-1]
        return list_insert[index_end-1]

    # 当数据量小于cut_off时，使用插入排序处理
    def sort_short_list(index_start, index_end):
        for index_1 in range(index_start + 1, index_end+1):
            num_temp = list_insert[index_1]
            index_2 = index_1
            while index_2 > index_start:
                if list_insert[index_2-1] > num_temp:
                    list_insert[index_2] = list_insert[index_2-1]
                    index_2 -= 1
                else:
                    break
            list_insert[index_2] = num_temp

    # 分
    def divide(index_start, index_end):
        if index_end - index_start < cut_off:
            sort_short_list(index_start, index_end)
        else:
            pivot = get_pivot(index_start, index_end)
            index_1, index_2 = index_start+1, index_end-2
            while index_1 <= index_end and index_2 >= index_start:
                while list_insert[index_1] < pivot:
                    index_1 += 1
                while list_insert[index_2] > pivot:
                    index_2 -= 1
                if index_2 <= index_1:
                    list_insert[index_1], list_insert[index_end-1] = list_insert[index_end-1], list_insert[index_1]
                    break
                else:
                    list_insert[index_1], list_insert[index_2] = list_insert[index_2], list_insert[index_1]
                    index_1 += 1
                    index_2 -= 1
            divide(index_start, index_1-1)
            divide(index_1+1, index_end)

    # cut_off 大于等于1
    cut_off = 5
    divide(0, len(list_insert)-1)


# 基数排序 次位优先 范围0-999
def radix_sort_LSD(list_insert):
    """"
    时间复杂度：O(p(n + b))
    稳定
    :param list_insert: 需要排序的列表，原地修改
    """
    buckets = [[] for i in range(10)]
    for num in list_insert:
        buckets[0].append(num)
    num_divisor_1 = 10
    num_divisor_2 = 1
    while num_divisor_1 <= 1000:
        buckets_new = [[] for i in range(10)]
        for bucket in buckets:
            for num in bucket:
                index_bucket = num % num_divisor_1
                index_bucket = index_bucket // num_divisor_2
                buckets_new[index_bucket].append(num)
        buckets = buckets_new
        num_divisor_2 = num_divisor_1
        num_divisor_1 *= 10
    index_1 = 0
    for bucket in buckets:
        for num in bucket:
            list_insert[index_1] = num
            index_1 += 1

import random

def equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            return False
    return True


def isSorted(list_1):
    for i in range(len(list_1)-1):
        if list_1[i] > list_1[i+1]:
            return False
    return True


def test():
    list_1 = list(range(-50, 51))
    list_2 = list(range(-50, 50))
    list_1.extend(list_2)
    list_2 = list_1.copy()
    list_2.sort()
    print("bubble_sort")
    random.shuffle(list_1)
    bubble_sort(list_1)
    print(equal(list_1, list_2))
    print("insertion_sort")
    random.shuffle(list_1)
    insertion_sort(list_1)
    print(list_1)
    print(equal(list_1, list_2))
    print("shell_sort")
    random.shuffle(list_1)
    shell_sort(list_1)
    print(list_1)
    print(equal(list_1, list_2))
    print("selection_sort")
    random.shuffle(list_1)
    selection_sort(list_1)
    print(list_1)
    print(equal(list_1, list_2))
    print("heap_sort")
    random.shuffle(list_1)
    heap_sort(list_1)
    print(list_1)
    print(equal(list_1, list_2))
    print("merge_sort")
    random.shuffle(list_1)
    merge_sort(list_1)
    print(list_1)
    print(equal(list_1, list_2))
    print("quick_sort")
    random.shuffle(list_1)
    list_3 = [10]*100
    quick_sort(list_1)
    print(list_1)
    print(equal(list_1, list_2))

    print("radix_sort_LSD")
    list_4 = []
    for i in range(100):
        list_4.append(random.randint(0, 999))
    radix_sort_LSD(list_4)
    print(list_4)
    print(isSorted(list_4))
    pass




if __name__ == "__main__":
    test()

