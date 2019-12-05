import sys

def get_evenodd_list():
    odd = []
    even = []
    
    num = input()
    while num != "-1":
        if int(num) % 2 == 0:
            even.append(int(num))
        else:
            odd.append(int(num))
        num = input()
    return (odd, even)