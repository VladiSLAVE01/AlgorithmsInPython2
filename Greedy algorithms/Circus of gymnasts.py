import sys
import heapq
from collections import Counter

def main():
    s = sys.stdin.readline().strip()
    if not s:
        print(0)
        return

    freq = Counter(s)
    heap = list(freq.values())
    heapq.heapify(heap)

    total = 0

    if len(heap) == 1:
        print(heap[0])
        return

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        total += a + b
        heapq.heappush(heap, a + b)

    print(total)


if __name__ == "__main__":
    main()