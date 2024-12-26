from utils import solve

class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}".format(self.val)

def calc(f):
    safe = 0
    for line in f:
        r = [int(x.strip()) for x in line.split(" ")]
        if verify(r):
            safe += 1
        else:
            for i in range(len(r)):
                cp = r.copy()
                del cp[i]
                if verify(cp):
                    safe += 1
                    break


    print(safe)



def verifyDampened(r):
    inc = False
    a, b = 0, 1
    skips = 0 
    while a < b and b < len(r):
        failed = False
        if r[a] == r[b]:
            failed = True

        if b == 1:
            if r[b] > r[a]:
                inc = True

        if r[b] > r[a] and not inc:
            failed = True
        
        if r[b] < r[a] and inc:
            failed = True

        diff = abs(r[b] - r[a])
        if diff < 1 or diff > 3:
            failed = True
    
        a += 1
        b += 1

        if failed:
            r.pop(b)

    return verify(r)

def verify(r):
    inc = False
    for i in range(1, len(r)):
        if r[i] == r[i-1]:
            return False

        if i == 1:
            if r[i] > r[i-1]:
                inc = True

        if r[i] > r[i-1] and not inc:
            return False
        
        if r[i] < r[i-1] and inc:
            return False

        diff = abs(r[i] - r[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

solve("day2.in", calc)
