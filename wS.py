def weave(str1, str2: str) -> str:
    result_string = ""
    i = 0

    while i != len(str1) and i != len(str2):
        result_string += str1[i] + str2[i]
        i += 1
    if i < len(str1):
        result_string += str1[i:]
    elif i > len(str2):
        result_string += str2[i:]
    return result_string
    
    



import sys
print(weave(sys.argv[1], sys.argv[2]))
