# write your code here

def compare(regex, input):
    if regex == '':
        return "True"
    if regex == '.':
        return "True"
    if regex == input:
        return "True"
    return "False"


if __name__ == "__main__":
    parameters = input().split('|')
    print(compare(parameters[0], parameters[1]))
