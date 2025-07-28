from collections import deque


class MinHeap(deque):
    def __init__(self, inp):
        super().__init__(inp)
        self.heap_size = 0

    def sift_down(self, i, index):
        self.heap_size = len(self)
        ind_l_child = 2 * i + 1
        ind_r_child = 2 * i + 2
        ind_largest = i
        if (
            ind_l_child <= self.heap_size - 1
            and self[ind_l_child][index] < self[ind_largest][index]
        ):
            ind_largest = ind_l_child
        if (
            ind_r_child <= self.heap_size - 1
            and self[ind_r_child][index] < self[ind_largest][index]
        ):
            ind_largest = ind_r_child
        if ind_largest != i:
            self[i], self[ind_largest] = self[ind_largest], self[i]
            self.sift_down(ind_largest, index)

    def build_heap(self, index):
        self.heap_size = len(self)
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.sift_down(i, index)

    def lpop(self, index):
        self[0], self[-1] = self[-1], self[0]
        tmp = self.pop()
        self.sift_down(0, index)
        return tmp


# создаем сортированный список lst символов по частотам
lst_inp = list(input())
dct = {}
for letter in lst_inp:
    dct[letter] = dct.get(letter, 0) + 1  # (letter, number)
lst = MinHeap(dct.items())
lst.build_heap(-1)

# генерируем бинарное дерево, сортированное по частотам, максимум в корне (https://habr.com/ru/articles/144200/)
while len(lst) > 1:
    l = lst.lpop(-1)
    r = lst.lpop(-1)
    lst.append([l, r, l[-1] + r[-1]])
lst = lst[0]
dct = {}


# добавляем в словарь dct пары буква:бинарный код проходя по дереву от корня
def set_code(lst, code=""):
    if isinstance(lst, tuple) == True:
        dct[lst[0]] = "0"
        return
    for i in range(len(lst)):
        if isinstance(lst[i], tuple) == True:
            dct[lst[i][0]] = code + str(i)
        else:
            if isinstance(lst[i], list) == True:
                set_code(lst[i], code + str(i))


set_code(lst)
len_dct = len(dct)

result = []
for letter in lst_inp:
    result.append(dct[letter])
result = "".join(result)
print(len_dct, len(result))
for letter in dct:
    print(f"{letter[0]}: {dct[letter[0]]}")
print(result)
