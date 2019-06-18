def is_pangram(sentence: str) -> bool:
    alpha_set=set(list("abcdefghijklmnopqrstuvwxyz "))
    input_sentence_set = set(list(sentence.lower()))
    return sorted(alpha_set) == sorted(input_sentence_set)


def cal_impurity_index(sentence: str) -> float:
    consonents = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    impurity_index = 0
    if len(list(sentence)) == 27:
        return 0
    for i in set(sentence):
        if i == " ":
            continue
        if sentence.count(i) > 1:
            if i in consonents:
                impurity_index += 0.7 * sentence.count(i)
            if i in vowels:
                impurity_index += 0.5 * sentence.count(i)
            if sentence.count(i) > 3:
                impurity_index += 3
            elif sentence.count(i) == 3:
                impurity_index += 1
    return impurity_index
                
                
    
    



print(is_pangram("Old brother fox jumps over the lazy dog"))
print(cal_impurity_index("Pack my box with five dozen liquor jugs"))
