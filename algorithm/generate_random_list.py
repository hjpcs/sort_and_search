import random


# 生成一个长度为length，范围在start-stop之间的整型数组
def generate_random_list(start, stop, length):
    if length >= 0:
        length = int(length)
    if start <= stop:
        start, stop = (int(start), int(stop))
    else:
        start, stop = (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


