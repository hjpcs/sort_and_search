# 希尔排序
def shell_sort(l):
    # 初始化gap值，一般采用序列长度的一半
    gap = (int)(len(l)/2)
    # 第一层循环：依次改变gap值对列表进行分组
    while (gap >= 1):
        # 下面利用直接插入排序的思想对分组数据进行排序
        # range(gap, len(l))：从gap开始
        for x in range(gap, len(l)):
            # range(x-gap, -1, -gap)：从x-gap开始与选定元素开始倒序比较，每个元素之间步长为gap
            for i in range(x-gap, -1, -gap):
                # 如果前一个元素大于后一个元素，则交换
                if l[i] > l[i+gap]:
                    temp = l[i+gap]
                    l[i+gap] = l[i]
                    l[i] = temp
        # while循环条件折半
        gap = (int)(gap/2)

list = [4169, 9061, 8003, 7439, 2175, 4568, 5158, 5879, 7594, 4177, 3098, 4521, 3445, 7245, 6139]
shell_sort(list)
print(list)