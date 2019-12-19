def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    comp = 0
    swapcount = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        comp += 1
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
            if i != 0:
                comp += 1
            swapcount += 1
    return comp, swapcount