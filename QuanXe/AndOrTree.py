import globals

all_state = []
def and_or_tree(state, step = 0):
    all_state.append(state)
    if len(state) == globals.N:
        if state == globals.target_solution:
            return state, all_state, step
        return None
    row = len(state)
    for col in range(globals.N):
        if col not in state:
            new_state = state + [col]
            result = and_or_tree(new_state, step+1)  # OR: thử tiếp
            if result:  # nếu tìm được 1 nhánh thành công thì trả về (AND-OR)
                return result
    return None