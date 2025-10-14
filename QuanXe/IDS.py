import globals
from DLS import DLS

def IDS():
    limit = 0
    text_box = []
    all_steps = 0
    while True:
        result, all_state, step = DLS(limit)
        all_steps += step
        if result is not None:
            text_box.append(f"state: {result}, limit: {limit}")
            return result, text_box, all_steps+limit
        else:
            text_box.append(f"state: None, limit: {limit}")
        limit += 1