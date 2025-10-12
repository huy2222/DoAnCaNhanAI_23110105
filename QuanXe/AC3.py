from collections import deque
import copy

def constraint(i, x, j, y):
    return x != y  # Chỉ cần khác cột
def revise(domains, Xi, Xj):
    revised = False
    for x in domains[Xi][:]:
        if not any(constraint(Xi, x, Xj, y) for y in domains[Xj]):
            domains[Xi].remove(x)
            revised = True
    return revised
def ac3(domains, variables):
    queue = deque((Xi, Xj) for Xi in variables for Xj in variables if Xi != Xj)
    while queue:
        Xi, Xj = queue.popleft()
        if revise(domains, Xi, Xj):
            if not domains[Xi]:
                return False
            for Xk in variables:
                if Xk not in (Xi, Xj):
                    queue.append((Xk, Xi))
    return True

def is_consistent(state, row, val):
    """Kiểm tra xem đặt quân hậu ở (row, val) có hợp lệ với các hàng trước không"""
    for r, c in enumerate(state):
        if not constraint(r, c, row, val):
            return False
    return True
def backtrackAC3(state, domains, variables,all_state=None,  step = 0):
    if all_state is None:
        all_state = []
    if len(state) == len(variables):
        return state, all_state, step
    row = len(state)
    for val in domains[row]:
        if is_consistent(state, row, val):
            new_state = state + [val]
            new_domains = copy.deepcopy(domains)
            new_domains[row] = [val]
            if ac3(new_domains, variables):
                all_state.append(new_state)
                result = backtrackAC3(new_state, new_domains, variables,all_state, step+1)
                if result:
                    return result
    return None,all_state, step
