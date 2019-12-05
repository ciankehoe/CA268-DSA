import sys

def get_odd_list():
    lst = []
    
    num = input()
    while num != "-1":
        if int(num) % 2 != 0:
            lst.append(int(num))
        num = input()
    return lst