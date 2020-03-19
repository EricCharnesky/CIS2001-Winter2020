import random

from HeapPriorityQueue import HeapPriorityQueue

heap_priority_queue = HeapPriorityQueue()

for n in range(100):
    heap_priority_queue.add(random.randint(1, 1000))

while len(heap_priority_queue) != 0:
    print(heap_priority_queue.remove_min())