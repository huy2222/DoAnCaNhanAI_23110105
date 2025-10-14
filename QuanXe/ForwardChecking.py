import globals
from NiemTin import check_rooks

def ForwardChecking(state, all_state=None, step = 0):
    if all_state is None:
        all_state = []
    if len(state) == globals.N:
        return state, all_state, step
    step+=1
    col = len(state)
    row_occupy = [row for row, col in state]
    domain = [row for row in range(globals.N) if row not in row_occupy]
    all_state.append(f"domain tai cot {col}: {domain} ")
    for row in domain:
        new_state = state.copy()
        new_state.append([row, col])
        if check_rooks(new_state):
            res = ForwardChecking(new_state, all_state, step)
            if res is not None:
                return res