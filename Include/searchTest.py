# 本文件中主要写的有关查找的一些方法

def binarySearch(arr, start, end, target):
    """
    二分查找法，寻找列表中与目标相同的元素下边
    :param arr:     列表
    :param start:   开始索引
    :param end:     结束索引
    :param target:  目标元素值
    :return:
    """
    if start <= end:
        # 获取中间索引
        mid = int(start + (end - start) / 2)
        # 如果中间值等于目标值，返回中间值的索引
        if arr[mid] == target:
            return mid
        # 如果中间值小于目标值，则对列表右半部分进行操作，需要将mid+1，因为mid的值已经比较过了
        elif arr[mid] < target:
            return binarySearch(arr, mid + 1, end, target)
        # 如果中间值大于目标值，则对列表左半部分进行操作，需要将mid-1，因为mid的值已经比较过了
        else:
            return binarySearch(arr, start, mid - 1, target)
    else:
        # 该元素不存在与给定列表中
        return -1


def search(arr, n, target):
    """
    线性查找，一个一个比对
    :param arr:     列表
    :param n:   列表最大索引
    :param target:  目标元素值
    :return:
    """
    for i in range(0, n):
        if arr[i] == target:
            return i
    else:
        return -1


arr = [6, 12, 23, 32, 34, 45, 84, 95]
target = 32

# 二分法查找
binary_search_index = binarySearch(arr, 0, len(arr) - 1, target)
if binary_search_index != -1:
    print('binary_search_index:', binary_search_index)
else:
    print('[二分查找]：目标元素在列表中不存在')

# 线性查找
search_index = search(arr, len(arr)-1, target)
if search_index != -1:
    print("search_index:", search_index)
else:
    print("[线性查找]：目标元素在列表中不存在")