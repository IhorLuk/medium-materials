from collections import deque
from time import perf_counter

# implement queues and stacks with in-built lists
list_queue = []
list_stack = []

for i in range(3):
    list_queue.insert(0, i)
    list_stack.append(i)

for i in range(3):
    print("Queue: " , list_queue.pop())
    print("Stack: ", list_stack.pop())

# now lets implement the same with deque
from collections import deque

queue = deque()
stack = deque()

for i in range(3):
    queue.append(i)
    stack.append(i)

for i in range(3):
    print("Queue: ", queue.popleft())
    print("Stack: ", stack.pop())


# compare speed for both deque and list with 10,000 iterations
t1 = perf_counter()

n = 400_000
for i in range(n):
    queue.append(i)

for i in range(n):
    queue.popleft()

t_queue = perf_counter() - t1
print("deque: ", perf_counter() - t1)

t1 = perf_counter()
for i in range(n):
    list_queue.insert(0, i)

for i in range(n):
    list_queue.pop()

t_list = perf_counter() - t1
print("list: ", perf_counter() - t1)
print(f"deque is {t_list / t_queue:.2f} times faster")


# the same but for stack operations
t1 = perf_counter()

for i in range(n):
    queue.append(i)

for i in range(n):
    queue.pop()

t_queue = perf_counter() - t1
print("stack with deque: ", perf_counter() - t1)

t1 = perf_counter()
for i in range(n):
    list_queue.append(i)

for i in range(n):
    list_queue.pop(0)

t_list = perf_counter() - t1
print("list: ", perf_counter() - t1)
print(f"stack with deque is {t_list / t_queue:.2f} times faster")