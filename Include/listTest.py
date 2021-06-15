# 列表联系

# 获取集合中最大的值
list = [13, 53, 25, 95, 12, 34, 83, 25]
list.sort(reverse=False)
print(list[-1])

# 合并字典
def Merge(dict1, dict2):
    return dict1.update(dict2)

dict1 = {'age': 5, 'sex': 'b'}
dict2 = {'name': 'zhangSan', 'friend': 'liSi'}
print(Merge(dict1, dict2))
print(dict1)