def find_root(lst, ind):
    if lst[ind] == ind:
        return ind
    else:
        lst[ind] = find_root(lst, lst[ind])
        return lst[ind]


def union(lst, ind_1, ind_2):
    root_1 = find_root(lst, ind_1)
    root_2 = find_root(lst, ind_2)
    if root_1 != root_2:
        lst[root_2] = root_1


n, e, d = [int(i) for i in input().split()]
lst = list(range(n))
for _ in range(e):
    num1, num2 = [int(i) - 1 for i in input().split()]
    union(lst, num1, num2)
flag = True
for _ in range(d):
    num1, num2 = [int(i) - 1 for i in input().split()]
    if find_root(lst, num1) == find_root(lst, num2):
        flag = False
        break
print(1 if flag else 0)
