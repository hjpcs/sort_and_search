from algorithm.generate_random_list import generate_random_list
import timeit
# 冒泡排序
def bubble_sort(l):
   length = len(l)
   # 序列长度为length，需要执行length-1轮交换
   for x in range(1, length):
       # 对于每一轮交换，都将序列中的左右元素进行比较
       # 每轮交换当中，由于序列最后的元素一定是最大的，因此每轮循环到序列未排序的位置即可
       for i in range(0, length-x):
           if l[i] > l[i + 1]:
               temp = l[i]
               l[i] = l[i+1]
               l[i+1] = temp


