seen = set()
dups = [] #duplicates

num = input().lstrip().strip() # read our input

while num != "-1":
    if num not in seen:
        seen.add(num)
    else:
        dups.append(num)
    num = input().lstrip().strip()

print("Enter numbers (-1 to end): " + ' '.join(dups) + " ")