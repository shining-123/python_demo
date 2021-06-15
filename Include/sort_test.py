# 这里主要写的是各种排序方法

def insertion_sort(arr, *order):
    """
    插入排序：以从大到小排序为例，拿着后一个元素值与前边元素进行一一对比，
            直到找到，比这个元素小的当前元素，然后讲这个元素插到当前元素后边
    :param arr: 需要排序的列表
    :return:
    """
    for i in range(1, len(arr)):
        flag = arr[i]  # 每次拿出的元素，目标数据
        j = i - 1   # 需要与目标数据进行比较的数据索引
        # 当j大于等于0，并且
        while j >= 0 and flag < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = flag

    # if bool(order) == True:
    #     for i in range(1, len(arr)):
    #         flag = arr[i]  # 每次拿出的元素，目标数据
    #         j = i - 1   # 需要与目标数据进行比较的数据索引
    #         # 当j大于等于0，并且
    #         while j >= 0 and flag < arr[j]:
    #             arr[j + 1] = arr[j]
    #             j -= 1
    #         arr[j + 1] = flag
    # else:
    #     for i in range(1, len(arr)):
    #         flag = arr[i]  # 每次拿出的元素，目标数据
    #         j = i - 1   # 需要与目标数据进行比较的数据索引
    #         # 当j大于等于0，并且
    #         while j >= 0 and flag > arr[j]:
    #             arr[j + 1] = arr[j]
    #             j -= 1
    #         arr[j + 1] = flag


def partition_index(arr, low, high):
    """
    快速排序中获取分隔索引
    :param arr:     原数组
    :param low:     开始索引
    :param high:    结束索引
    :return:
    """
    pi = low   # 分隔点索引
    for j in range(low, high):
        if arr[pi] > arr[j]:
            arr[pi+1], arr[j] = arr[j], arr[pi+1]
            arr[pi], arr[pi+1] = arr[pi+1], arr[pi]
            pi += 1
    return pi

def divide_sort(arr, low, high):
    """
    快速排序，取一个分隔元素，比该元素大的放到该元素的左边，比该元素小的放到该元素的右边，依次递归
    :param arr:     原数组
    :param low:     开始索引
    :param high:    结束索引
    :return:
    """
    if low < high-1:
        pi = partition_index(arr, low, high)    # 获取到当前排序阶段的分隔索引

        divide_sort(arr, pi+1, high)
        divide_sort(arr, low, pi)   # 这个地方不减一是因为rang()方法不包括pi

def select_sort(arr, low, high):
    """
    选择排序，每次找到为排序中最小的元素放到前边，以此类推
    :param arr:     原数组
    :param low:     开始索引
    :param high:    结束索引
    :return:
    """
    for i in range(low, high):
        min = arr[i]
        min_index = i
        for j in range(i, high):
            if arr[j]<min:
                min = arr[j]
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]


arr1 = [56, 24, 9, 17, 94, 61, 77, 38]
insertion_sort(arr1)
print('插入排序后的数组')
print(arr1[0: len(arr1)])

# arr[0], arr[1] = arr[1], arr[0] # 第一个元素和第二个元素互换位置
# print(arr[0: len(arr)-1])

# 快速排序
arr2 = [56, 53, 13, 17, 27, 61, 77, 38]
divide_sort(arr2, 0, len(arr2))
print('快速排序后的数组')
print(arr2[0: len(arr2)])

# 选择排序
arr3 = [56, 53, 13, 93, 27, 61, 77, 38]
select_sort(arr3, 0, len(arr3))
print('选择排序后的数组')
print(arr3[0: len(arr3)])