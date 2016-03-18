from stack import Stack

b = "{}[]()}"
def to_list(b):
    l = []
    for s in b:
        l.append(s)
    return l

l = to_list(b)

def brackets(l):
    s = Stack()
    openers = ["(", "{", "["]

    oc = {")":"(", "}":"{","]":"["}
    #Check if list is empty
    if l == None:
        return True
    #Check if list is even
    elif len(l) % 2 == 1:
        return False
    else:
        for i in l:
            if i in openers:
                s.push(i)
            else:
                if oc[i] in openers:
                    s.pop()
                else: return False
        if s.peek() == None:
            return True

print(brackets(l))
