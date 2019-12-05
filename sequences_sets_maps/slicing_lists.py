def get_sliced_lists(lst):
    lists = []
    minus_last = lst[:-1]
    minus_first_last = lst[1:-1]
    reverse_list = lst[::-1]
    lists.append(minus_last)
    lists.append(minus_first_last)
    lists.append(reverse_list)
    return lists