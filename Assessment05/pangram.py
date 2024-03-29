def is_pangram(sentence: str) -> bool:
    alpha_set=set("abcdefghijklmnopqrstuvwxyz ")
    input_sentence_set = set(sentence.lower())
    return sorted(alpha_set) == sorted(input_sentence_set)


def cal_impurity_index(sentence: str):
    consonents = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    impurity_index = 0
    if is_pangram(sentence):
        if len(list(sentence)) == 27:
            return 0
        for i in set(sentence):
            if i == " ":
                continue
            if sentence.count(i) > 1:
                if i in consonents:
                    impurity_index += 0.7
                if i in vowels:
                    impurity_index += 0.5
                if sentence.count(i) > 3:
                    impurity_index += 3
                elif sentence.count(i) == 3:
                    impurity_index += 1
        return impurity_index
    else:
        return "not a pangram!!"
                
                    



print(is_pangram("Old brother fox jumps over the lazy dog"))
print(cal_impurity_index("Old brother fox jumps over the lazy dog"))
