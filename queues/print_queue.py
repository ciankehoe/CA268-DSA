from Queue import Queue

def print_queue(lst, front, back):
    if back < front:
        return lst[front:] + lst[:back]
    elif front < back:
        return lst[front:back]