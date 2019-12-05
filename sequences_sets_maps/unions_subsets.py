def set_stuff(a, b):
    union = a.union(b)
    a_sub_b = a.issubset(b)
    a_super_b = a.issuperset(b)
    return (union, a_sub_b, a_super_b)