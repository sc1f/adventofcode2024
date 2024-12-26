# from heapq import heapify, heappush, heappop
import os

left, right = [], []

file_path = os.path.join(os.path.dirname(__file__), "day1")
with open(file_path, "r") as in_file:
    for line in in_file:
        nums = line.split("   ")
        left.append(int(nums[0].strip()))
        right.append(int(nums[-1].strip()))

left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])

print(dist)

from collections import defaultdict
from utils import solve

def calc(f):
    left, right = [], []
    counts = defaultdict(int)
    for line in f:
        nums = line.split("   ")
        left.append(int(nums[0].strip()))
        r = int(nums[-1].strip())
        right.append(r)
        counts[r] += 1

    score = 0
    for n in left:
        score += (n * counts[n])
    print(score)


solve("day1", calc)