phone_book = {}

print("Enter a name and number, or a name and ? to query (!! to exit)")

query = input().strip()

while query != "!!":
    name, q = query.split()

    if name not in phone_book and q != "?":
        phone_book[name] = q
    
    elif name in phone_book and q != "?":
        phone_book[name] = q

    elif q == "?" and name in phone_book:
        print('{} has number {}'.format(name, phone_book[name]))

    else:
        #name not in phone_book and q == "?":
        print("Sorry, there is no " + name)
    
    query = input().strip()

print("Bye")