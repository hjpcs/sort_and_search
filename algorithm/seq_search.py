def seq_search(l, data):
    length = len(l)
    for x in range(0, length):
        if l[x] == data:
            return f'{data}是list中第{x+1}个数'
    return 'list中没有这个数'


list = [4169, 9061, 8003, 7439, 2175, 4568, 5158, 5879, 7594, 4177, 3098, 4521, 3445, 7245, 6139]
print(seq_search(list, 6139))