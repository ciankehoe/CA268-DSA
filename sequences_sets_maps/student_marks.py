import sys

def make_map():

    students = {}

    info = input()
    name, marks = info.split()

    try:
        while True:
            students[name] = marks
            name, marks = input().split()
    except:
        return students