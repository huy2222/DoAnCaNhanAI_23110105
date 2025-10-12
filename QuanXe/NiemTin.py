import globals
def check_rooks(state):
    rows = set()
    cols = set()
    for row, col in state:
        if row in rows or col in cols:
            return False  # trùng hàng hoặc cột
        rows.add(row)
        cols.add(col)
    return True


def MoveNiemTin(state):
    new_state = []
    for row, col in state:
        new_col = (col + 1) % globals.N
        new_state.append([row, new_col])
    return new_state


def DatNiemTin(state):
    """Thêm 1 quân xe mới vào cột kế tiếp"""
    col = len(state)
    for row in range(globals.N):
        new_state = state + [[row, col]]
        if check_rooks(new_state):
            return new_state
    return state  # nếu không đặt được thì trả lại


def Niemtin():
    # ban đầu 1 nghiệm gồm 2 trạng thái: [] và [[0,1]]
    stack = [[[], [[0, 1]]]]
    result = []
    step = 0
    all_state = []
    while stack:
        state_group = stack.pop()  # 1 nghiệm
        new_group = []
        step+=1
        for st in state_group:
            if len(st) == globals.N and check_rooks(st):
                # if len(result) == 10:
                #     return result  # tìm được nghiệm đủ N quân hợp lệ
                # else:
                #     result.append(st)
                return st, all_state, step
            # sinh 2 trạng thái mới từ st
            moved = MoveNiemTin(st)
            added = DatNiemTin(st)

            if check_rooks(moved):
                new_group.append(moved)
                all_state.append(moved)
            if check_rooks(added):
                new_group.append(added)
                all_state.append(added)

        if new_group:
            stack.append(new_group)

    return None