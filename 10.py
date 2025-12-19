# PART 1
from collections import deque
lines = open("10.txt", "r").read().split("\n")
res = 0
for line in lines:
    sp = line.split()
    ind = sp[0]
    ind = [c=="#" for c in ind[1:-1]]
    but = [list(map(int, c[1:-1].split(","))) for c in sp[1:-1]]
    q = deque()
    q.append([[0] * len(ind), 0]) # [indicator state, number of presses]
    mem = set()
    while q:
        state, presses = q.popleft()
        state_tup = tuple(state)
        if state_tup in mem:
            continue
        mem.add(state_tup)
        if state == ind:
            res += presses
            break
        for b in but:
            new_state = state[:]
            for i in b:
                new_state[i] = not new_state[i]
            q.append([new_state, presses + 1])
print(res)

# PART 2
# linear programming bash
from ortools.linear_solver import pywraplp

res = 0
for line in lines:
    sp = line.split()
    # min number of presses such that sum of activations equals jolt
    but = [list(map(int, c[1:-1].split(","))) for c in sp[1:-1]]
    jolt = list(map(int, sp[-1][1:-1].split(",")))
    x = []
    solver = pywraplp.Solver.CreateSolver('CBC')
    for i in range(len(but)):
        x.append(solver.IntVar(0, solver.infinity(), f'x{i}'))
    for j in range(len(jolt)):
        ct = solver.Constraint(jolt[j], jolt[j])
        for i in range(len(but)):
            if j in but[i]:
                ct.SetCoefficient(x[i], 1)
    objective = solver.Objective()
    for i in range(len(but)):
        objective.SetCoefficient(x[i], 1)
    objective.SetMinimization()
    status = solver.Solve()
    res += int(objective.Value())
print(res)