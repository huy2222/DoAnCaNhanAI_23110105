from queue import PriorityQueue

import globals
def Path_Cost_Greedy(stateNow):
    hx = 0
    for i in range(len(globals.target_solution)):
        if i > len(stateNow) - 1:
            hx += globals.target_solution[i]
        else:
            hx += abs(stateNow[i] - globals.target_solution[i])
    hx += (globals.N - len(stateNow))
    return hx
def Greedy():
    hangdoi = PriorityQueue()
    hangdoi.put((0, []))  # (cost, state)
    step = 0
    all_state = []
    while not hangdoi.empty():
        cost, state = hangdoi.get()
        step += 1
        all_state.append(state)
        if state == globals.target_solution:
            return state, all_state, step
        if len(state) == globals.N:
            continue
        col = len(state)
        for row in range(globals.N):
            if row not in state:
                new_state = state + [row]
                new_cost = Path_Cost_Greedy(new_state)
                hangdoi.put((new_cost, new_state))
    return None