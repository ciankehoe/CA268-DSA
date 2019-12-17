from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            if self.table[index].is_empty():
                # Only add it if not already there (this is a set)
                self.table[index].add(item)
                return None
            else:
                # this has detected that there exists a value in this chain / entry already
                # but we still want to add our new item to it
                self.table[index].add(item)
                return(index, item)