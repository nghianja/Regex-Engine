# write your code here

def compare(regex, input):
    if regex == '':
        return True
    if regex == '.':
        return True
    if regex == input:
        return True
    return False


def comparator(regex, input):
    if regex == '':
        return True
    if input == '':
        return False
    if compare(regex[0], input[0]) is False:
        return False
    return comparator(regex[1:], input[1:])


def regular_express(regex, input):
    if regex == '':
        return True
    for i in range(len(input)):
        if comparator(regex, input[i:]) is True:
            return True
    return False


if __name__ == "__main__":
    parameters = input().split('|')
    print(regular_express(parameters[0], parameters[1]))
