new_word = ""
vowels = ["a", "e", "i", "o", "u"]
def pig_latin(word):
    for letter in word:
        if letter[0] not in vowels:
            for x in range(1, len(letter)):
                if letter[x] in vowels:
                    new_word = letter[x:len(letter)] + letter[0:x] + "ay"
                    break
        else:
            new_word = letter + "way"
            
        print(new_word, end = " ")

word = str(input("Input word: ")).split(" ")
pig_latin(word)