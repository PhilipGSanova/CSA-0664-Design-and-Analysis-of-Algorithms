def rev(string):
    if len(string) == 0:
        return string
    else:
        return rev(string[1:]) + string[0]

input_string = "Hello"
reversed_string = rev(input_string)
print(reversed_string)  