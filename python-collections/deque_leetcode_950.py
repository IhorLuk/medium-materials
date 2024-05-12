from time import perf_counter
from collections import deque

deck = [17,13,11,2,3,5,7,12,1,4,54,53,52,78]

# list for queue approach
def process_list(deck):
    t1 = perf_counter()

    N = len(deck)
    tmp_deck = sorted(deck)

    output = [0] * N
    idx_queue = list(range(N))#deque(range(N))
    pick = True

    i = 0
    while idx_queue:
        
        if pick:
            output[idx_queue.pop(0)] = tmp_deck[i]
            i += 1
            pick = False
        else:
            idx_queue.append(idx_queue.pop(0))
            pick = True

    t_list = perf_counter() - t1
    return t_list

# deque approach
def process_deque(deck):
    t1 = perf_counter()
    tmp_deck = sorted(deck)
    N = len(deck)
    deck.sort()

    output = [0] * N
    idx_queue = deque(range(N))
    pick = True

    i = 0
    while idx_queue:
        if pick:
            output[idx_queue.popleft()] = tmp_deck[i]
            i += 1
            pick = False
        else:
            idx_queue.append(idx_queue.popleft())
            pick = True

    t_queue = perf_counter() - t1
    return t_queue

times_repeat = 100_000
times_list = [process_list(deck) for i in range(times_repeat)]
times_deque = [process_deque(deck) for i in range(times_repeat)]

print(f"{(sum(times_list) / times_repeat) / (sum(times_deque) / times_repeat):.2f}")