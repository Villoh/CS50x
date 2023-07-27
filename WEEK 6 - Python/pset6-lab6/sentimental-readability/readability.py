def count_letters(text):
    letters = 0
    # Loop through every character of the text
    for char in text:
        # When a letter is found (A-Z/a-z), increment the letters count
        if char.isalpha():
            letters += 1
    return letters


def count_words(text):
    words = 1
    # Loop through every character of the text
    for char in text:
        # When a space is found, increment the words count
        if char.isspace():
            words += 1
    return words


def count_sentences(text):
    sentences = 0
    # Loop through every character of the text
    for char in text:
        # When a dot, exclamation mark, or question mark is found, increment the sentences count
        if char in ['.', '!', '?']:
            sentences += 1
    return sentences


def get_grade(letters, words, sentences):
    # Coleman-Liau formula
    index = round(0.0588 * (letters / words) * 100 - 0.296 * (sentences / words) * 100 - 15.8)
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade", index)


def main():
    # Ask the user to type a text
    text = input("Text: ")
    # Call the get_grade function
    get_grade(count_letters(text), count_words(text), count_sentences(text))


if __name__ == "__main__":
    main()
