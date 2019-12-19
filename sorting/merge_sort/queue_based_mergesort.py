from Queue import Queue

def split(q):
    """ A split function which will split a queue into two.
        The function returns a tuple containing the two queues.
    """
    initial_length = len(q)
    
    q1 = Queue()
    q2 = Queue()
    
    i = 0
    while i < initial_length // 2:
        q1.enqueue(q.dequeue())
        i += 1
    
    while i < initial_length:
        q2.enqueue(q.dequeue())
        i += 1
    
    return(q1, q2)