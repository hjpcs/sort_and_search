# 快速排序
def qucik_sort(l, left, right):
    # left排序开始的index，right序列末尾的index，pivot选取的基准数
    # 对于长度为length的序列：left = 0；right = length-1
    if left < right:
        i, j, pivot = left, right, l[left]
        while i < j:
            # 从右开始向左寻找第一个小于pivot的值
            while (i < j) and (l[j] >= pivot):
                j -= 1
            # 将小于pivot的值移到左边
            if (i < j):
                l[i] = l[j]
                i += 1
            # 从左开始向右寻找第一个大于pivot的值
            while (i < j) and (l[i] < pivot):
                i += 1
            # 将大于pivot的值移到右边
            if (i < j):
                l[j] = l[i]
                j -= 1
        # 循环结束后，说明 i = j，此时左边的值全都小于pivot，右边的值全都大于pivot
        # pivot的位置移动正确，那么此时只需对左右两侧的序列调用此函数进一步排序即可
        # 递归调用函数：依次对左侧序列：从left ~ i-1   右侧序列：从i+1 ~ right排序
        l[i] = pivot
        # 左侧序列继续排序
        qucik_sort(l, left, i-1)
        # 右侧序列继续排序
        qucik_sort(l, i+1, right)

list = [4169, 9061, 8003, 7439, 2175, 4568, 5158, 5879, 7594, 4177, 3098, 4521, 3445, 7245, 6139]
qucik_sort(list, 0, len(list)-1)
print(list)
