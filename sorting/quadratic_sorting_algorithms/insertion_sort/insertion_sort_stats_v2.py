def insertion_sort(lst):
    comp = 0
    moves = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        moves += 1
        comp += 1
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
            moves += 1
            if i != 0:
                comp += 1

        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        moves += 1
    return comp, moves