def title_case(sentence, key_word):
    words = []
    word = ''
    count = 0
    while True:
        if sentence[count] != ' ' :
            word += sentence[count]
            print(word, count, len(sentence))
        elif count == len(sentence) or sentence[count] == ' ':
            words.append(word)
            word = ''

        count += 1
        if count == len(sentence):
            break

    print(words)



title_case('a clash of KINGS', 'a an the of')