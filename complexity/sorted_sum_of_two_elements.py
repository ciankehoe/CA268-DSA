def sum_to_k(lst, k):
    i, j = 0, len(lst) - 1
    while i != j:
        total = lst[i] + lst[j]
        if total == k:
            return True
            i += 1
        if total > k:
            j -= 1
        if total < k:
            i += 1
    return False
