# 简单选择排序
def select_sort(l):
    # 依次遍历序列中每一个元素
    for x in range(0, len(l)):
        # 将当前位置的元素定义为此轮循环中的最小值
        min = l[x]
        # 将该元素与剩下的元素依次比较寻找最小元素
        for i in range(x+1, len(l)):
            if l[i] < min:
                temp = l[i]
                l[i] = min
                min = temp
        # 将比较后得到的真正的最小值赋给当前位置
        l[x] = min

list = [4169, 9061, 8003, 7439, 2175, 4568, 5158, 5879, 7594, 4177, 3098, 4521, 3445, 7245, 6139]
select_sort(list)
print(list)