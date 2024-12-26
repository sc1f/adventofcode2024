from collections import defaultdict
from functools import cmp_to_key
from utils import solve

def validate(rules, update):
    idx = {page: position for position, page in enumerate(update)}
    for node, children in rules.items():
        if node not in idx:
            continue
        for child in children:
            if child in idx and idx[node] > idx[child]:
                return False
    return True

def sort_update(rules, update):
    def compare(a,b):
        if b in rules[a]:
            return -1
        if a in rules[b]:
            return 1
        return 0
    return sorted(update, key=cmp_to_key(compare))
            
def middle_number(rules, update):
    if not validate(rules, update):
        fixed = sort_update(rules, update)
        return fixed[len(fixed) // 2]
    # return update[len(update) // 2]
    return 0
        

def calc(f):
    rules = defaultdict(set)
    updates = []
    for line in f:
        if "|" in line:
            s = line.split("|")
            rules[int(s[0].strip())].add(int(s[1].strip()))
        if "," in line:
            updates.append([int(n.strip()) for n in line.split(",")])

    middle_sum = 0
    for update in updates:
        middle_sum += middle_number(rules, update)

    print(middle_sum)

solve("day5.in", calc)