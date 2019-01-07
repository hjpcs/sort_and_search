from algorithm.generate_random_list import generate_random_list
import timeit
# 归并排序
# 这是合并的函数，将序列l[first...mid]与序列l[mid+1...last]合并
def merge_array(l, first, mid, last, temp):
    i, j, k = first, mid+1, 0
    # 当左右两边都有数时进行比较，取较小的数
    while (i <= mid) and (j <= last):
        if l[i] <= l[j]:
            temp[k] = l[i]
            i += 1
            k += 1
        else:
            temp[k] = l[j]
            j += 1
            k += 1
    # 如果左边序列还有数
    while (i <= mid):
        temp[k] = l[i]
        i += 1
        k += 1
    # 如果右边序列还有数
    while (j <= last):
        temp[k] = l[j]
        j += 1
        k += 1
    # 将temp当中该段有序元素赋值给l待排序列使之部分有序
    for x in range(0, k):
        l[first + x] = temp[x]

# 这是分组的函数
def group_array(l, first, last, temp):
    if first < last:
        mid = (int)((first + last) / 2)
        # 使左边序列有序
        group_array(l, first, mid, temp)
        # 使右边序列有序
        group_array(l, mid+1, last, temp)
        # 将两个有序序列合并
        merge_array(l, first, mid, last, temp)

# 归并排序的函数
def merge_sort(l):
    # 声明一个长度为len(l)的空列表
    temp = len(l) * [None]
    # 调用函数
    group_array(l, 0, len(l)-1, temp)

random_list = generate_random_list(0, 100000, 100000)
#print(random_list)
#list = [4169, 9061, 8003, 7439, 2175, 4568, 5158, 5879, 7594, 4177, 3098, 4521, 3445, 7245, 6139]
start = timeit.default_timer()
merge_sort(random_list)
end = timeit.default_timer()
#print(random_list)
print(f'{end-start}')
start = timeit.default_timer()
sorted(random_list)
end = timeit.default_timer()
print(f'{end-start}')
