from queue import PriorityQueue
import globals
def Path_Cost(stateNow):
    return globals.N - len(stateNow)
def UCS():
    hangdoi = PriorityQueue()
    hangdoi.put((Path_Cost([]), []))  # (cost, state)
    step=0
    all_state = []
    while not hangdoi.empty():
        cost, state = hangdoi.get()
        step += 1
        all_state.append(f"state: {state} -- cost: {cost}")
        if state == globals.target_solution:
            return state, all_state,step
        if len(state) == globals.N:
            continue
        col = len(state)
        for row in range(globals.N):
            if row not in state:
                new_state = state + [row]
                new_cost = Path_Cost(new_state)
                hangdoi.put((new_cost, new_state))
    return None