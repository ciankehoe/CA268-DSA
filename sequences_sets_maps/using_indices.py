def get_counts(lst):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for word in lst:
        counts[len(word)] += 1
    return counts