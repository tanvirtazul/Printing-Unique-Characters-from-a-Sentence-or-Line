def IfFound(character, lst): # searching a character item from the list. If found, return true, else false.
    found = False

    for item in lst:
        if character == item: 
            found = True
            return found

    return found    


def UniqueCharacters(sentence):
    size = len(sentence)
    print(size)

    lst = []

    for c in sentence:
        if IfFound(c, lst) == False:
            if c != " " and c != "?" and c != "." and c != ":" and c != ";" and c != "/" and c != ",":
                lst.append(c)

    return lst


print("Please enter a sentence/line: ")
sentence = input()
a = UniqueCharacters(sentence)
print(a)