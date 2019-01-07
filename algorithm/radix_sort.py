# 基数排序
# 确定排序的次数
# 排序的顺序跟序列中最大数的位数相关


def radix_sort_nums(l):
    max_num = l[0]
    # 寻找序列中的最大数
    for x in l:
        if max_num < x:
            max_num = x
    # 确定序列中的最大元素的位数
    times = 0
    while (max_num > 0):
        max_num = (int)(max_num / 10)
        times += 1
    return times


# 找到num从低到高第pos位的数据
def get_num_pos(num, pos):
    return ((int)(num / (10 ** (pos-1)))) % 10


# 基数排序
def radix_sort(l):
    count = 10 * [None]       # 存放各个桶的数据统计个数
    bucket = len(l) * [None]  # 暂时存放排序结果
    # 从低位到高位依次执行循环
    for pos in range(1, radix_sort_nums(l)+1):
        # 置空各个桶的数据统计
        for x in range(0, 10):
            count[x] = 0
        # 统计当前该位(个位，十位，百位....)的元素数目
        for x in range(0, len(l)):
            # 统计各个桶将要装进去的元素个数
            j = get_num_pos(int(l[x]), pos)
            count[j] += 1
        # count[i]表示第i个桶的右边界索引
        for x in range(1, 10):
            count[x] += count[x-1]
        # 将数据依次装入桶中
        for x in range(len(l)-1, -1, -1):
            # 求出元素第pos位的数字
            j = get_num_pos(l[x], pos)
            # 放入对应的桶中，count[j]-1是第j个桶的右边界索引
            bucket[count[j] - 1] = l[x]
            # 对应桶的装入数据索引-1
            count[j] -= 1
        # 将已分配好的桶中数据再倒出来，此时已是对应当前位数有序的表
        for x in range(0, len(l)):
            l[x] = bucket[x]

list = [4169, 9061, 8003, 7439, 2175, 4568, 5158, 5879, 7594, 4177, 3098, 4521, 3445, 7245, 6139]
radix_sort(list)
print(list)