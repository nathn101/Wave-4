keyList = []
def reverseLookup(list, item):
    for key in list:
        if list[key] == item:
            keyList.append(key)
        else:
            continue
    print(keyList)

dictionary = {"letterA": "a", "letterB": "b", "letterC": "c", "First_Alphabet_Letter": "a"}

reverseLookup(dictionary, "a")