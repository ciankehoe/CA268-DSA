def even_count(lst):
    count = 0
    ptr = lst.head
    while ptr != None:
        if ptr.item % 2 == 0:
            count += 1
            ptr = ptr.next
        else:
            ptr = ptr.next
    return count