import math
import random
from Tools.demo.sortvisu import steps
import globals
def Path_Cost_HillClimbing(stateNow):
    hx = 0
    for i in range(len(globals.target_solution)):
        if i > len(stateNow) - 1:
            hx += globals.target_solution[i]
        else:
            hx += abs(stateNow[i] - globals.target_solution[i])
    return hx
def SimulatedAnnealing():
    # Khởi tạo state ngẫu nhiên
    state = [random.randint(0, globals.N - 1) for _ in range(globals.N)]
    step = 0
    all_state = []
    T = 100.0
    Tmin = 1e-3
    alpha = 0.99
    while T > Tmin:
        step+=1
        all_state.append(state)
        if state == globals.target_solution:
            return state, all_state, step
        neighbor = state[:]
        neighbor[random.randint(0, globals.N - 1)] = random.randint(0, globals.N - 1)
        dentaE = Path_Cost_HillClimbing(neighbor) - Path_Cost_HillClimbing(state)
        if dentaE <= 0:
            state = neighbor
        else:
            P = math.exp(-dentaE / T)
            if random.random() < P:
                state = neighbor
        T *= alpha

    return state