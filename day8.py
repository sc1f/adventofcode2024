from collections import defaultdict
from utils import solve

def calc(f):
    locations = defaultdict(list)
    for row, line in enumerate(f):
        items = list(line.strip())
        for col, item in enumerate(items):
            if item != ".":
                locations[item].append((row, col))
    
    print(locations)

solve("day8.in.small.2", calc)