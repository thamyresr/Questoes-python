list_words = []

try:
    with open('file.txt', 'r') as file:
        for text in file:
            for word in text:
                list_words.append(word)

    list_words.reverse()

    for text in list_words:
        print(text, end='')

except FileNotFoundError as error:
    print(error)
