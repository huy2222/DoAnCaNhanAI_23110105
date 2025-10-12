from collections import deque
import copy

# Số quân hậu
N = 4
steps = 0  # Biến toàn cục đếm số bước

def constraint(i, x, j, y):
    """Hai quân hậu không được cùng cột và không cùng đường chéo"""
    return x != y and abs(i - j) != abs(x - y)

def revise(domains, Xi, Xj):
    """Loại bỏ các giá trị trong domain[Xi] không thỏa mãn ràng buộc với Xj"""
    revised = False
    for x in domains[Xi][:]:
        if not any(constraint(Xi, x, Xj, y) for y in domains[Xj]):
            domains[Xi].remove(x)
            revised = True
            print(f"⚠️  AC3 loại bỏ {x} khỏi domain[{Xi}] vì không còn giá trị hợp lệ với X{Xj}")
    return revised

def ac3(domains, variables):
    """Thuật toán AC3: duy trì tính nhất quán cung"""
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
    """Kiểm tra xem (row, val) có hợp lệ với các hàng trước không"""
    for r, c in enumerate(state):
        if not constraint(r, c, row, val):
            return False
    return True

def print_domains(domains):
    """In ra toàn bộ domain hiện tại"""
    print("   📘 Domain hiện tại:")
    for k, v in domains.items():
        print(f"      Hàng {k}: {v}")
    print("-" * 40)

def backtrack(state, domains, variables):
    global steps
    steps += 1

    print(f"\n🔹 Bước {steps}: Gán cho hàng {len(state)} | Trạng thái hiện tại: {state}")
    print_domains(domains)

    if len(state) == len(variables):
        return state  # ✅ Tất cả quân hậu đã được đặt

    row = len(state)
    for val in domains[row]:
        if is_consistent(state, row, val):
            new_state = state + [val]
            new_domains = copy.deepcopy(domains)
            new_domains[row] = [val]

            print(f"👉 Thử đặt quân hậu ở (hàng={row}, cột={val})")
            if ac3(new_domains, variables):
                result = backtrack(new_state, new_domains, variables)
                if result:
                    return result
            else:
                print(f"⛔ AC3 phát hiện miền trống sau khi gán hàng {row}={val}, quay lui...")

    print(f"🔙 Quay lui từ trạng thái {state}")
    return None

# ---------------------------
# Khởi tạo và chạy
# ---------------------------
variables = list(range(N))
domains = {i: list(range(N)) for i in variables}

solution = backtrack([], domains, variables)
print("\n✅ Kết quả cuối cùng:")
print("Solution:", solution)
print("Tổng số bước:", steps)
