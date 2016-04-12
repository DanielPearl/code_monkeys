# Determines the end parenthesis of a string given the index of the first parenthesis

string = "3(sd(f(sd)fhgjhg)h))gthg"

def parenthesis_index(string, idx):
    """
    :param string: string
    :param idx: index of the opening parenthesis
    :returns: index of the closing parenthesis given the opening parenthesis
    """
    parenthesis = 0
    if string[idx] == "(":
        for i in range(idx, len(string)):
            if string[i] == "(":
                parenthesis += 1
            if string[i] == ")":
                parenthesis -= 1
                if parenthesis == 0:
                    return i
    return None

print(parenthesis_index(string, 1))
