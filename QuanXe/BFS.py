from collections import deque
import globals

def BFS():
    hangdoi = deque([[]])
    all_state = []
    step = 0
    while hangdoi:
        state = hangdoi.popleft()
        step+=1
        all_state.append(state)
        if state == globals.target_solution:
            return state,all_state, step
        if len(state) == globals.N:
            continue
        col = len(state)
        for row in range(globals.N):
            if row not in state:
                new_state = state + [row]
                hangdoi.append(new_state)

    return None