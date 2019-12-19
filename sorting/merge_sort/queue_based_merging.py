from Queue import Queue

def merge(q1, q2, q):
    """ this function will merge q1 and q2 into q.
        Assuming that q1 and q2 are sorted, this function will
        return q such that q contains the combined elements of q1 and q2 and
        q will also be sorted.
        
        The function returns nothing. The result will be contained in the queue parameter.
    """
    # q1 = len of 6
    # q2 = len of 5
    i = q1.dequeue()
    j = q2.dequeue()
    while (q1.isempty() is False) and (q2.isempty() is False):
        #if q1.first() < q2.first():
        #    q.enqueue(q1.dequeue)
        #else:
        #    q.enqueue(q2.dequeue)
        if i < j:
            q.enqueue(i)
            i = q1.dequeue()
        else:
            q.enqueue(j)
            j = q2.dequeue()

    if i < j:
        q.enqueue(i)
        q.enqueue(j)
    else:
        q.enqueue(j)
        q.enqueue(i)

    while q2.isempty() is False:
        q.enqueue(q2.dequeue())

    while q1.isempty() is False:
        q.enqueue(q1.dequeue())