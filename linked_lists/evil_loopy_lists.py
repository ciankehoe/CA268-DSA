def detect_loop(ll):
    head = ll.head
    ptr = ll.head
    while ptr != None:
        next_ptr = ptr.next
        if next_ptr == head:
                return True
        else:
            ptr = ptr.next
    return False