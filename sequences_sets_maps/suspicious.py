import sys

students = sys.argv[1]
delinq = sys.argv[2]

d = {}

with open(students) as f:
    for line in f:
    #    name = f.readline().strip()
        d[line.strip()] = 0

with open(delinq) as p:
    for line in p:
    #    name = p.readline().strip()
        if line.strip() in d:
            d[line.strip()] += 1

both = 0
for key, value in sorted(d.items()):
    if value > 0:
        both += 1
        print('{}. {}'.format(both,key))