class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)
#
#
#
    def recursive_count(self, ptr, lo, hi):
        if ptr == None:
            return 0
        if ptr.item >= lo and ptr.item <= hi:
            return self.recursive_count(ptr.left, lo, hi) + self.recursive_count(ptr.right, lo, hi) + 1
        else:
            return self.recursive_count(ptr.left, lo, hi) + self.recursive_count(ptr.right, lo, hi)
                
    def count(self, hi, lo):
        return self.recursive_count(self.root, hi, lo)

    def height(self):
        return self.recursive_height(self.root)

    def recursive_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return max(self.recursive_height(ptr.right), self.recursive_height(ptr.left)) + 1
    
    def total(self):
        return self.recursive_total(self.root)

    def recursive_total(self, ptr):
        if ptr == None:
            return 0
        else:
            return self.recursive_total(ptr.right) + self.recursive_total(ptr.left) + ptr.item