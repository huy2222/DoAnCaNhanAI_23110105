import globals
from NiemTin import check_rooks


def MoveNiemTinMotPhan(state, statePos):
    new_state = []
    for row, col in state:
        if [row, col] in statePos:
            new_state.append([row, col])
            continue
        new_col = (col + 1) % globals.N
        new_state.append([row, new_col])
    return new_state


def DatNiemTinMotPhan(state):
    # """Thêm 1 quân xe mới vào cột kế tiếp"""
    for row in range(globals.N):
        for col in range(globals.N):
            if [row, col] not in state:
                new_state = state + [[row, col]]
                if check_rooks(new_state):
                    return new_state
    return state


def NiemTinMotPhan(statePos):
    # Nếu truyền 1 quân đơn, bọc lại thành [[row,col]]
    if isinstance(statePos[0], int):  # ví dụ [0,4]
        init_state = [statePos]
    else:  # ví dụ [[0,0],[1,1]]
        init_state = statePos
    stack = [init_state]  # stack chứa các trạng thái
    result = []
    step = 0
    all_state = []
    while stack:
        st = stack.pop()  # lấy ra 1 trạng thái
        step += 1
        if len(st) == globals.N and check_rooks(st):
            return st, all_state, step
        # sinh 2 trạng thái mới từ st
        moved = MoveNiemTinMotPhan(st, statePos)
        added = DatNiemTinMotPhan(st)

        if check_rooks(moved):
            stack.append(moved)
            all_state.append(moved)
        if check_rooks(added):
            stack.append(added)
            all_state.append(moved)
    return result if result else None