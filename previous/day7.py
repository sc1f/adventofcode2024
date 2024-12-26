from utils import solve

def concat(left, right):
    return int(str(left) + str(right))

class Equation:
    def __init__(self, answer, operators):
        self.answer = answer
        self.operators = operators

    def __str__(self):
        return f"{self.operators} = {self.answer}"
    
    def validate(self):
        def sum_operators(index, running_sum):
            if running_sum == self.answer:
                return True
            if index >= len(self.operators):
                return False
            currval = self.operators[index]
            return sum_operators(index + 1, running_sum + currval) or sum_operators(index + 1, running_sum * currval) or sum_operators(index + 1, concat(running_sum, currval))
        return sum_operators(0, 0)

def calc(f):
    equations = []
    for line in f:
        eq = line.split(":")
        answer = int(eq[0].strip())
        operators = [int(x.strip()) for x in eq[1].strip().split(" ")]
        eq = Equation(answer, operators)
        equations.append(eq)

    count = 0
    for eq in equations:
        if eq.validate():
            count += eq.answer
    print(count)

solve("day7.in.small", calc)