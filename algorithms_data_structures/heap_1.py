from collections import deque


class MinHeap(list):
    def __init__(self, inp):
        super().__init__(inp)

    def sift_down(self, i):
        ind_l_child = 2 * i + 1
        ind_r_child = 2 * i + 2
        ind_smallest = i
        if ind_l_child <= self.heap_size - 1 and self[ind_l_child] < self[ind_smallest]:
            ind_smallest = ind_l_child
        if ind_r_child <= self.heap_size - 1 and self[ind_r_child] < self[ind_smallest]:
            ind_smallest = ind_r_child
        if ind_smallest != i:
            self[i], self[ind_smallest] = self[ind_smallest], self[i]
            self.sift_down(ind_smallest)

    def build_heap(self):
        self.heap_size = len(self)
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.sift_down(i)


n, m = [int(i) for i in input().split()]
lst_task = deque([int(j) for j in input().split()])
time = 0
heap = MinHeap([])
for proc_n in range(n):
    heap.append((0, proc_n))
heap.build_heap()


while lst_task:
    print(heap[0][1], heap[0][0])
    heap[0] = (heap[0][0] + lst_task.popleft(), heap[0][1])
    heap.sift_down(0)
