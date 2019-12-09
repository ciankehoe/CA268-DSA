def check_brackets(line):
    brackets = "{[()]}"
    # removes any non-bracket characters as we don't need to check them
    s = ''.join([b for b in line if b in brackets])
    
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(s[i])
            
        if len(stack) == 0:
            return False
        
        if s[i] == ")":
            x = stack.pop()
            if (x == "{") or (x == "["):
                return False
        elif s[i] == "}":
            x = stack.pop()
            if (x == "(") or ("["):
                return False
        elif s[i] == "]":
            x = stack.pop()
            if (x == "{") or (x == "("):
                return False
    if len(stack):
        return False
    else:
        return True