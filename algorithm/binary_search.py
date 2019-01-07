def binary_search(l, data):
    length = len(l)
    first = 0
    last = length - 1
    while first <= last:
        mid = (int)((first + last) / 2)
        if l[mid] > data:
            last = mid - 1
        elif l[mid] < data:
            first = mid + 1
        else:
            return f'{data}是list中第{mid+1}个数'
    return 'list中没有这个数'

list = [2175, 3098, 3445, 4169, 4177, 4521, 4568, 5158, 5879, 6139, 7245, 7439, 7594, 8003, 9061]
print(binary_search(list, 6139))

