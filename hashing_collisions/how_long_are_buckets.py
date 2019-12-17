from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity
        self.count_nodes = 0
        self.buckets = 0

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList()
            self.buckets += 1
            # Need a new linked list for this entry

        if item not in self.table[index]:
            self.count_nodes += 1
            if self.table[index].is_empty():
                # Only add it if not already there (this is a set)
                self.table[index].add(item)
    
    def average_bucket_length(self):
        return(self.count_nodes / self.buckets)