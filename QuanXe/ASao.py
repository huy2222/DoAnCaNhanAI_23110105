from queue import PriorityQueue

import globals
def Path_Cost_ASao(stateNow):
    hx = 0
    for i in range(len(globals.target_solution)):
        if i > len(stateNow) - 1:
            hx += globals.target_solution[i]
        else:
            hx += abs(stateNow[i] - globals.target_solution[i])
    gx = len(stateNow)
    return hx + gx
def ASao():
    hangdoi = PriorityQueue()
    hangdoi.put((Path_Cost_ASao([]), []))  # (cost, state)
    step = 0
    all_state = []
    while not hangdoi.empty():
        cost, state = hangdoi.get()
        step += 1
        all_state.append([f"state: {state}, cost: {cost}"])
        if state == globals.target_solution:
            return state, all_state, step
        if len(state) == globals.N:
            continue
        col = len(state)
        for row in range(globals.N):
            if row not in state:
                new_state = state + [row]
                new_cost = Path_Cost_ASao(new_state)
                hangdoi.put((new_cost, new_state))
    return None

