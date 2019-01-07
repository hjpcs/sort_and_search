# 堆排序
# 获取左右叶子节点


def LEFT(i):
    return 2*i + 1


def RIGHT(i):
    return 2*i + 2
# 调整大顶堆
# l:待调整序列 length:序列长度 i:需要调整的结点


def adjust_max_heap(l, length, i):
    # 定义一个int值保存当前序列最大值的下标
    largest = i
    # 执行循环操作：两个任务：1.寻找最大值的下标；2.最大值与父节点交换
    while (1):
        # 获得序列左右叶子节点的下标
        left, right = LEFT(i), RIGHT(i)
        # 当左叶子节点的下标小于序列长度并且左叶子节点的值大于父节点时，将左叶子节点的下标赋值给largest
        if (left < length) and (l[left] > l[i]):
            largest = left
            print('左叶子节点')
        else:
            largest = i
        # 当右叶子节点的下标小于序列长度并且右叶子节点的值大于父节点时，将右叶子节点的下标值赋值给largest
        if (right < length) and (l[right] > l[largest]):
            largest = right
            print('右叶子节点')
        # 如果largest不等于i 说明当前的父节点不是最大值，需要交换值
        if (largest != i):
            temp = l[i]
            l[i] = l[largest]
            l[largest] = temp
            i = largest
            print(largest)
            continue
        else:
            break


# 建立大顶堆
def build_max_heap(l):
    length = len(l)
    for x in range((int)((length-1) / 2), -1, -1):
        adjust_max_heap(l, length, x)


# 堆排序
def heap_sort(l):
    # 先建立大顶堆，保证最大值位于根节点；并且父节点的值大于叶子结点
    build_max_heap(l)
    # i：当前堆中序列的长度.初始化为序列的长度
    i = len(l)
    # 执行循环：1. 每次取出堆顶元素置于序列的最后(len-1,len-2,len-3...)
    #          2. 调整堆，使其继续满足大顶堆的性质，注意实时修改堆中序列的长度
    while (i > 0):
        temp = l[i-1]
        l[i-1] = l[0]
        l[0] = temp
        # 堆中序列长度减1
        i -= 1
        # 调整大顶堆
        adjust_max_heap(l, i, 0)


list = [4169, 9061, 8003, 7439, 2175, 4568, 5158, 5879, 7594, 4177, 3098, 4521, 3445, 7245, 6139]
heap_sort(list)
print(list)