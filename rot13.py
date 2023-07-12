def rot13(message):
    # Clearly define both uppercase and lowercase letters in one string
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    answer = ""

    """ Enumerate through the given message and compare each character to the position in
    'str1' and 'str2' """
    for ind, c in enumerate(message):
        if c in str1:
            capIndex = str1[str1.index(c) + 13]
            answer += capIndex
        elif c in str2:
            lowIndex = str2[str2.index(c) + 13]
            answer += lowIndex
        else:
            answer += c
    print(answer)
    return answer

while True:
    provided_input = input("Please provide encoded ROT13 message:\n")
    rot13(provided_input)
