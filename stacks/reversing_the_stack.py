from Stack import Stack

def reverse_input(stack):
    # Your code here
    # Read the input
    line = input().strip()
    try:
        while True:
            stack.push(line)
            line = input().strip()
    except:
        while stack.is_empty() != True:
            print(stack.pop())
    # place on the stack
    # print from the stack