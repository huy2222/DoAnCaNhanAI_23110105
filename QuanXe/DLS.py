from Tools.demo.sortvisu import steps

import globals
def DLS(limit):
    stack = [[]]
    step = 0
    all_state = []
    while stack:
        state = stack.pop()
        step += 1
        all_state.append(state)
        k = len(state)
        if k > limit:
            continue
        if state == globals.target_solution:
            return state, all_state, step
        if len(state) == globals.N:
            continue
        col = len(state)
        for row in range(globals.N - 1, -1, -1):
            if row not in state:
                new_state = state + [row]
                stack.append(new_state)
    return None, all_state, step
