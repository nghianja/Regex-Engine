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


if __name__ == "__main__":
    parameters = input().split('|')
    print(comparator(parameters[0], parameters[1]))
