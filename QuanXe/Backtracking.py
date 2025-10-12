import globals
from NiemTin import check_rooks

def Backtracking(state, all_state=None, step = 0):
    if all_state is None:
        all_state = []
    all_state.append(state)
    step+=1
    if len(state) == globals.N:
        return state, all_state, step
    col = len(state)
    for row in range(globals.N):
        if [row, col] not in state:
            new_state = state.copy()
            new_state.append([row, col])
            if check_rooks(new_state):
                res = Backtracking(new_state, all_state, step)
                if res is not None:
                    return res