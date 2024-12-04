import re
from utils import open_input

r1 = "mul\((\d+),(\d+)\)"
r2 = "mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"

def calc(f):
    muls = re.findall(r2, f.read())
    res = 0
    mul = True
    for m in muls:
        if m[2] == "do()":
            mul = True
        if m[3] == "don't()":
            mul = False
        if m[0] != "" and m[1] != "" and mul:
            res += (int(m[0]) * int(m[1]))
    print(res)

open_input("day3.in", calc)