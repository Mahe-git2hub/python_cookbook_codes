# Can split an interable into multiple parts
a, b, c = [1, 2, 3]
print(a, b, c)

print('-' * 25)

# Unpacking Elements from Iterables of Arbitrary Length
# In this example we want to compare current sales against previous sales
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("trailing : ", trailing)

print('-' * 25)

# Keeping the Last N Items
from collections import deque

q = deque(maxlen=4)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
q.append(5)
print(q)
q.append(6)
print(q)
q.append(7)
print(q)
q.append(8)
print(q)

print('-' * 25)

# Finding the Largest or Smallest N Items
from heapq import nlargest, nsmallest
from random import randint

ranNos = [randint(1, 100) for _ in range(65)]
print("Entire array :", ranNos)
print("Smallest 15 elements of array :", nsmallest(15, ranNos))
print("Largest 15 elements of array :", nlargest(15, ranNos))

print('-' * 25)

# Implementing a Priority Queue
import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
