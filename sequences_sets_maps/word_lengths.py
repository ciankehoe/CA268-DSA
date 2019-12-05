def get_counts_dict(lst):
    
    d = {}

    for word in lst:
        if len(word) not in d:
            d[len(word)] = 1
        else:
            d[len(word)] += 1
    return d