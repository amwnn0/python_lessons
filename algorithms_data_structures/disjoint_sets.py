max_size = 0


def find_root(lst, ind):
    if lst[ind][1] == ind:
        return ind
    else:
        lst[ind][1] = find_root(lst, lst[ind][1])
        return lst[ind][1]


def union(lst, ind_1, ind_2):
    global max_size
    root_1 = find_root(lst, ind_1)
    root_2 = find_root(lst, ind_2)
    if root_1 != root_2:
        lst[root_1][0] = lst[root_1][0] + lst[root_2][0]
        if lst[root_1][0] > max_size:
            max_size = lst[root_1][0]
        lst[root_2][1] = root_1


n, m = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]
for i in range(len(lst)):
    if lst[i] > max_size:
        max_size = lst[i]
    lst[i] = [lst[i], i]


for _ in range(m):
    ind1, ind2 = [(int(i) - 1) for i in input().split()]
    union(lst, ind1, ind2)
    print(max_size)
