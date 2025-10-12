import globals


def DFS():
    stack = [[]]
    all_state = []
    step = 0
    while stack:
        state = stack.pop()
        all_state.append(state)
        step += 1
        if state == globals.target_solution:
            return state, all_state, step
        if len(state) < globals.N:
            row = len(state)
            for col in range(globals.N - 1, -1, -1):
                if col not in state:
                    stack.append(state + [col])
    return None