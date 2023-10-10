while True:
    input_words = input("Please enter two words: ")
    
    if input_words.lower() == 'done':
        print("-- bye !!")
        break

    words = input_words.split()
    
    if len(words) == 2:
        word1, word2 = words
        if word1 < word2:
            print(word1, "comes first")
        else:
            print(word2, "comes first")
    elif len(words) == 1:
        pass
