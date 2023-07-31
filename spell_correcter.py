from spellchecker import SpellChecker


def correct_word(word):
    spell = SpellChecker()

    # Convert the word to lowercase (optional)
    word = word.lower()

    # Check if the word is spelled correctly
    if spell.correction(word) == word:
        return word
    else:
        # If misspelled, return the nearest word
        return spell.correction(word)


if __name__ == "__main__":
    # Take input from the user
    word_to_check = input("Enter a word to check its spelling: ")
    corrected_word = correct_word(word_to_check)
    print(f"Original Word: {word_to_check}")
    print(f"Corrected Word: {corrected_word}")
