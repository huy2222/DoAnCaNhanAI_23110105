import globals
def Path_Cost_HillClimbing(stateNow):
    hx = 0
    for i in range(len(globals.target_solution)):
        if i > len(stateNow) - 1:
            hx+=globals.target_solution[i]
        else:
            hx += abs(stateNow[i] - globals.target_solution[i])
    return hx


def HillClimbing():
    state = []
    cost = Path_Cost_HillClimbing(state)
    step = 0
    all_state = []
    while True:
        step += 1
        all_state.append(f"state: {state} -- cost: {cost}")
        if state == globals.target_solution:
            return state, all_state, step
        if len(state) == globals.N:
            break
        col = len(state)
        best_state = None
        best_cost = cost
        for row in range(globals.N):
            if row not in state:
                new_state = state + [row]
                new_cost = Path_Cost_HillClimbing(new_state)
                if new_cost <= best_cost:  # càng lớn thì càng giống đích
                    best_cost = new_cost
                    best_state = new_state
        if best_state is None:
            break
        else:
            state = best_state
            cost = best_cost
    return state