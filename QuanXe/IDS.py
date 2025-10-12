import globals
from DLS import DLS

def IDS():  # Dò tìm k phù hợp IDS
    limit = 0
    text_box = []
    all_steps = 0
    while True:
        result, all_state, step = DLS(limit)
        # stated.append(f"state cuoi: {result} ,limit: {limit} ")
        all_steps += step
        if result is not None:
            text_box.append(f"state: {result}, limit: {limit}")
            # print("Giá trị limit là:", limit)
            # print("GT result:", result)
            return result, text_box, all_steps+limit
        else:
            text_box.append(f"state: None, limit: {limit}")
        limit += 1