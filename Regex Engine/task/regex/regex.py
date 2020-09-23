# write your code here

def compare(regex, input):
    if regex == '' or regex == '.' or regex == input:
        return True
    return False


def comparator(regex, input):
    if regex == '':
        return True
    if regex == '$' and input == '':
        return True
    if input == '':
        return False
    if len(regex) > 1:
        if regex[0] == '\\':
            if compare(regex[1], input[0]) is True:
                return comparator(regex[2:], input[1:])
            else:
                return False
        if (regex[1] == '?' or regex[1] == '*') and compare(regex[0], input[0]) is False:
            return comparator(regex[2:], input)
        if regex[1] == '?' and compare(regex[0], input[0]) is True:
            return comparator(regex[2:], input[1:])
        if regex[1] == '*' or regex[1] == '+':
            i = 0
            while compare(regex[0], input[i]) is True:
                i += 1
                if i >= len(input) or input[i] != input[i-1]:
                    break
            if i > 0:
                return comparator(regex[2:], input[i:])
    if compare(regex[0], input[0]) is False:
        return False
    return comparator(regex[1:], input[1:])


def regular_express(regex, input):
    if regex == '':
        return True
    if regex[0] == '^':
        return comparator(regex[1:], input)
    for i in range(len(input)):
        if comparator(regex, input[i:]) is True:
            return True
    return False


if __name__ == "__main__":
    parameters = input().split('|')
    print(regular_express(parameters[0], parameters[1]))
