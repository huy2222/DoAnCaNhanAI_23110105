import math
import time
import tkinter as tk
from collections import deque
from inspect import stack
from queue import PriorityQueue
import random
from turtledemo.penrose import start


import globals
from ASao import ASao
from AndOrTree import and_or_tree
from BFS import BFS
from Backtracking import Backtracking
from BeamSearch import BeamSearch
from DFS import DFS
from DLS import DLS
from ForwardChecking import ForwardChecking
from GeneticAlgorithm import GeneticAlgorithm, Fitness
from Greedy import Greedy
from HillClimbing import HillClimbing
from MotphanNiemTin import NiemTinMotPhan
from NiemTin import Niemtin
from SimulatedAnnealing import SimulatedAnnealing
from UCS import UCS
from IDS import IDS
from AC3 import backtrackAC3

N = 8
CELL = 50
global target_solution
chiphi = 0
allchiphi = []


def BFS_XE():
    solution = []
    hangdoi = deque([[]])
    while hangdoi:
        state = hangdoi.popleft()
        if len(state) == N:
            solution.append(state)
            continue
        col = len(state)
        for row in range(N):
            if row not in state:
                new_state = state + [row]
                hangdoi.append(new_state)
    return solution

def draw_board(canvas, queens=None):
    canvas.delete("all")
    colors = ["white", "gray"]
    # Vẽ bàn cờ trước
    for row in range(N):
        for col in range(N):
            x1 = col * CELL
            y1 = row * CELL
            x2 = x1 + CELL
            y2 = y1 + CELL
            color = colors[(row + col) % 2]
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    # Nếu có quân xe thì vẽ chậm từng con một
    if queens:
        def draw_one(i=0):
            if i < len(queens):
                col, row = i, queens[i]
                x = col * CELL + CELL // 2
                y = row * CELL + CELL // 2
                canvas.create_text(x, y, text="♖", font=("Arial", 28), fill="red")
                # sau 300ms thì vẽ con tiếp theo
                canvas.after(300, draw_one, i + 1)

        draw_one(0)


def random_target():
    global target_solution
    target_solution = all_solutions[random.randint(1000, 30000)]
    globals.target_solution = target_solution
    draw_board(banphai, queens=target_solution)
    draw_board(bantrai)
    txt_log_right.insert("end", f"Target: {target_solution}\n")
def DrawPerformance(name, step, time, all_state):
    global txt_name, txt_time, txt_step
    txt_name.config(text=str(name))
    txt_time.config(text="Time: " +str(round(time, 8)))
    txt_step.config(text="Step: " +str(step))
    txt_log_left.delete("1.0", "end")
    txt_log_left.insert("end", "10 state cuối:\n")
    for state in all_state[-10:]:
        txt_log_left.insert("end", f"{state}\n")
def PerformanceMeasurement(algorithm, *args):
    # start_time = time.time()
    # state_result, all_state, step = algorithm(*args)
    # end_time = time.time()
    # elapsed = end_time - start_time
    start_time = time.perf_counter()
    state_result, all_state, step = algorithm(*args)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    return state_result, all_state, step, elapsed

def run_dfs():
    state_result, all_state, step, elapsed = PerformanceMeasurement(DFS)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("DFS", step, elapsed, all_state)
def run_bfs():
    state_result, all_state, step, elapsed = PerformanceMeasurement(BFS)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("BFS",step,elapsed, all_state)
def run_ucs():
    state_result, all_state, step, elapsed = PerformanceMeasurement(UCS)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("UCS", step, elapsed, all_state)
def run_dls():
    limit = 8
    state_result, all_state, step, elapsed = PerformanceMeasurement(DLS, limit)
    if state_result is None:
        all_state = [f"Voi limit = {limit} khong tim ra ket qua"]
    else:
        draw_board(bantrai, queens=state_result)
        txt_log_left.insert("end", f"LIMIT = {limit}\n")
    DrawPerformance("DLS", step, elapsed, all_state)

# chưa làm IDS
def run_ids():
    state_result, all_state, step, elapsed = PerformanceMeasurement(IDS)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("IDS", step, elapsed, all_state)
def run_greedy():
    state_result, all_state, step, elapsed = PerformanceMeasurement(Greedy)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("Greedy", step, elapsed, all_state)

def run_asao():
    state_result, all_state, step, elapsed = PerformanceMeasurement(ASao)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("A*", step, elapsed, all_state)


def run_hillClimbing():
    state_result, all_state, step, elapsed = PerformanceMeasurement(HillClimbing)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("Hill Climbing", step, elapsed, all_state)
    # print(HillClimbing())


def run_geneticAlgorithm():
    state_result, all_state, step, elapsed = PerformanceMeasurement(GeneticAlgorithm,Fitness, BFS_XE()[:20], target_solution, 3000, 15)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("GeneticAlgorithm", step, elapsed, all_state)
    # draw_board(bantrai, queens=GeneticAlgorithm())


def run_simulatedAnnealing():
    state_result, all_state, step, elapsed = PerformanceMeasurement(SimulatedAnnealing)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("Simulated Annealing", step, elapsed, all_state)
#

def run_Beam():
    state_result, all_state, step, elapsed = PerformanceMeasurement(BeamSearch, 5)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("Beam Search", step, elapsed, all_state)


def run_AND_OR():
    state_result, all_state, step, elapsed = PerformanceMeasurement(and_or_tree, [])
    # print("and: ", state_result)
    draw_board(bantrai, queens=state_result)
    DrawPerformance("And Or Tree", step, elapsed, all_state)


def run_niemtin():
    state_result, all_state, step, elapsed = PerformanceMeasurement(Niemtin)
    DrawPerformance("Belief State Search", step, elapsed, all_state)
    # state = Niemtin()
    # state = random.choice(state)
    sorted_state = sorted(state_result, key=lambda x: x[1])
    rows = [row for row, col in sorted_state]
    draw_board(bantrai, queens=rows)


def run_niemtinmotphan():
    state_result, all_state, step, elapsed = PerformanceMeasurement(NiemTinMotPhan, [[0, 0],[1, 7]])
    DrawPerformance("Partial Observation", step, elapsed, all_state)
    sorted_state = sorted(state_result, key=lambda x: x[1])
    rows = [row for row, col in sorted_state]
    # print("1phan: ", rows)
    draw_board(bantrai, queens=rows)


def run_backtracking():
    state_result, all_state, step, elapsed = PerformanceMeasurement(Backtracking, [])
    DrawPerformance("Backtracking", step, elapsed, all_state)
    sorted_state = sorted(state_result, key=lambda x: x[1])
    rows = [row for row, col in sorted_state]
    draw_board(bantrai, queens=rows)

def run_forwardChecking():
    state_result, all_state, step, elapsed = PerformanceMeasurement(ForwardChecking, [])
    DrawPerformance("Fun Backtracking", step, elapsed, all_state)
    sorted_state = sorted(state_result, key=lambda x: x[1])
    rows = [row for row, col in sorted_state]
    draw_board(bantrai, queens=rows)
def run_ac3():
    state_result, all_state, step, elapsed = PerformanceMeasurement(backtrackAC3, [], {v: list(range(N)) for v in list(range(N))}, list(range(N)))
    DrawPerformance("AC3", step, elapsed, all_state)
    draw_board(bantrai, queens=state_result)
def main():
    global root, bantrai, banphai, all_solutions, target_solution, txt_log_left, txt_log_right
    global txt_name, txt_step, txt_time
    root = tk.Tk()
    root.title("8 quân xe")
    all_solutions = BFS_XE()
    # target_solution = all_solutions[random.randint(1, 100)]
    target_solution =  [4, 5, 0, 6, 3, 1, 2, 7]
    globals.target_solution = target_solution
    print("target: ", target_solution)

    # === Khung chứa 2 bàn cờ và log dưới mỗi bàn cờ ===
    board_frame = tk.Frame(root, bg="#f0f8ff")
    board_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    # Bàn cờ bên trái + log
    left_frame = tk.Frame(board_frame, bg="#f0f8ff")
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    bantrai = tk.Canvas(left_frame, width=N * CELL, height=N * CELL, bg="white")
    bantrai.pack()
    draw_board(bantrai)

    log_frame_left = tk.Frame(left_frame)  # frame chứa Text + Scrollbar
    log_frame_left.pack(pady=5, fill="both", expand=True)

    txt_log_left = tk.Text(log_frame_left, width=50, height=15,bg="white", fg="black", font=("Consolas", 12))
    txt_log_left.pack(side="left", fill="both", expand=True)
    scroll_left = tk.Scrollbar(log_frame_left, command=txt_log_left.yview)
    scroll_left.pack(side="right", fill="y")
    txt_log_left.config(yscrollcommand=scroll_left.set)

    txt_log_left.insert("end", "Log bàn cờ trái...\n")



    # Bàn cờ bên phải + log
    right_frame = tk.Frame(board_frame, bg="#f0f8ff")
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    banphai = tk.Canvas(right_frame, width=N * CELL, height=N * CELL, bg="white")
    banphai.pack()
    draw_board(banphai, queens=target_solution)

    log_frame_right = tk.Frame(right_frame)  # frame chứa Text + Scrollbar
    log_frame_right.pack(pady=5, fill="both", expand=True)

    txt_log_right = tk.Text(log_frame_right, width=50, height=6, bg="white", fg="black", font=("Consolas", 10))
    txt_log_right.pack(side="left", fill="both", expand=True)

    scroll_right = tk.Scrollbar(log_frame_right, command=txt_log_right.yview)
    scroll_right.pack(side="right", fill="y")
    txt_log_right.config(yscrollcommand=scroll_right.set)

    txt_log_right.insert("end", f"Target: {target_solution}\n")
    txt_log_right.insert("end", "Chương trình bắt đầu...\n")

    # === Control frame bên cột 2 ===
    control_frame = tk.Frame(root)
    control_frame.grid(row=0, column=2, padx=20, pady=0, sticky="n")


     # Style chung cho các nút
    btn_style = {
        "font": ("Helvetica", 11, "bold"),
        "fg": "white",
        "relief": "raised",
        "bd": 2,
        "activebackground": "#357ae8",
        "activeforeground": "white",
        "cursor": "hand2"
    }
    search_frame = tk.LabelFrame(
        control_frame,
        text="Tìm kiếm KHÔNG thông tin",
        padx=10,
        pady=10,
        fg="#1a1a1a",
        bg="#e8f0fe",  # nền nhạt xanh dương nhẹ
        font=("Helvetica", 12, "bold")
    )
    search_frame.pack(fill="x", pady=10)

    # Tạo từng nút với màu khác nhau một chút
    btn_dfs = tk.Button(search_frame, text="DFS", bg="#4285F4", command=run_dfs, **btn_style)
    btn_dfs.pack(fill="x", pady=5)

    btn_bfs = tk.Button(search_frame, text="BFS", bg="#4285F4", command=run_bfs, **btn_style)
    btn_bfs.pack(fill="x", pady=5)

    btn_ucs = tk.Button(search_frame, text="UCS", bg="#4285F4", command=run_ucs, **btn_style)
    btn_ucs.pack(fill="x", pady=5)

    btn_dls = tk.Button(search_frame, text="DLS", bg="#4285F4", command=run_dls, **btn_style)
    btn_dls.pack(fill="x", pady=5)

    btn_ids = tk.Button(search_frame, text="IDS",  command=run_ids, bg="#4285F4", **btn_style)
    btn_ids.pack(fill="x", pady=5)

    other_frame = tk.LabelFrame(control_frame, text="Khác", padx=10, pady=10,fg="#1a1a1a",bg="#e8f0fe", font=("Helvetica", 12, "bold"))
    other_frame.pack(fill="x", pady=10)
    btn_random = tk.Button(other_frame, text="Random Target",bg="#EA4335",  command=random_target, **btn_style, )
    btn_random.pack(fill="x", pady=5)

    performance_frame = tk.LabelFrame(control_frame, text="Hiệu suất thuật toán", padx=10, pady=10,fg="#1a1a1a",bg="#e8f0fe", font=("Helvetica", 12, "bold"))
    performance_frame.pack(fill="x", pady=10)
    txt_name = tk.Label(performance_frame, text="Tên Thuật toán: ", font=("Arial", 14))
    txt_name.pack(pady=10)
    txt_step = tk.Label(performance_frame, text="Bước: ", font=("Arial", 14))
    txt_step.pack(pady=10)
    txt_time = tk.Label(performance_frame, text="Time: ", font=("Arial", 14))
    txt_time.pack(pady=10)


    # === Control frame bên cột 3 ===
    control_frame_2 = tk.Frame(root)
    control_frame_2.grid(row=0, column=3, padx=20, pady=0, sticky="n")

    search_frame_2 = tk.LabelFrame(control_frame_2, text="Tìm kiếm CÓ thông tin", padx=10, pady=10,fg="#1a1a1a",bg="#e8f0fe", font=("Helvetica", 12, "bold"))
    search_frame_2.pack(fill="x", pady=10)
    btn_greedy = tk.Button(search_frame_2, text="Greedy", command=run_greedy, bg="#246709", **btn_style)
    btn_greedy.pack(fill="x", pady=5)
    btn_asao = tk.Button(search_frame_2, text="A*", command=run_asao, bg="#246709", **btn_style)
    btn_asao.pack(fill="x", pady=5)

    search_frame_3 = tk.LabelFrame(control_frame_2, text="LocalSearch", padx=10, pady=10,fg="#1a1a1a",bg="#e8f0fe", font=("Helvetica", 12, "bold"))
    search_frame_3.pack(fill="x", pady=10)
    btn_hillClimb = tk.Button(search_frame_3, text="Hill Climbing", command=run_hillClimbing, bg="#2823BD", **btn_style)
    btn_hillClimb.pack(fill="x", pady=5)
    btn_Gen = tk.Button(search_frame_3, text="Gen", command=run_geneticAlgorithm, bg="#2823BD", **btn_style)
    btn_Gen.pack(fill="x", pady=5)
    btn_Simulate = tk.Button(search_frame_3, text="Simulate", command=run_simulatedAnnealing, bg="#2823BD", **btn_style)
    btn_Simulate.pack(fill="x", pady=5)
    btn_Beam = tk.Button(search_frame_3, text="Beam", command=run_Beam, bg="#2823BD", **btn_style)
    btn_Beam.pack(fill="x", pady=5)

    search_frame_4 = tk.LabelFrame(control_frame_2, text="Complex Search", padx=10, pady=10,fg="#1a1a1a",bg="#e8f0fe", font=("Helvetica", 12, "bold"))
    search_frame_4.pack(fill="x", pady=10)
    btn_AndOrTree = tk.Button(search_frame_4, text="And Or Tree", command=run_AND_OR, bg="#3D1543", **btn_style)
    btn_AndOrTree.pack(fill="x", pady=5)
    btn_Niemtin = tk.Button(search_frame_4, text="Belief State Search", command=run_niemtin, bg="#3D1543", **btn_style)
    btn_Niemtin.pack(fill="x", pady=5)
    btn_NiemtinMotPhan = tk.Button(search_frame_4, text="Partial Observation", command=run_niemtinmotphan, bg="#3D1543", **btn_style)
    btn_NiemtinMotPhan.pack(fill="x", pady=5)

    search_frame_5 = tk.LabelFrame(control_frame_2, text="Constraint-Based Search", padx=10, pady=10,fg="#1a1a1a",bg="#e8f0fe", font=("Helvetica", 12, "bold"))
    search_frame_5.pack(fill="x", pady=10)
    btn_Backtracking = tk.Button(search_frame_5, text="Backtracking", command=run_backtracking, bg="#9C27B0", **btn_style)
    btn_Backtracking.pack(fill="x", pady=5)
    btn_forwardChecking = tk.Button(search_frame_5, text="Forward Checking", command=run_forwardChecking, bg="#9C27B0", **btn_style)
    btn_forwardChecking.pack(fill="x", pady=5)
    btn_Ac3 = tk.Button(search_frame_5, text="AC3", command=run_ac3, bg="#9C27B0", **btn_style)
    btn_Ac3.pack(fill="x", pady=5)

    root.mainloop()



if __name__ == "__main__":
    main()
