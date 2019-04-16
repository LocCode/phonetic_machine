# Lists of vowels and consonants in English language
eng_vowels = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
              'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
              'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
eng_consonants = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']


# Получаем вводимое пользователем слово
def get_english_word(word):
    letters = len(word)
    vowels = count_vowels(word)
    consonants = count_consonants(word)
    # Здесь хранится вся информация о слове
    result = [letters, vowels, consonants]

    return result


def count_vowels(word):
    word = list(word)
    common_vowels = []
    for a in word:
        for b in eng_vowels:
            if a == b:
                common_vowels.append(a)

    return common_vowels


def count_consonants(word):
    word = list(word)
    common_consonants = []
    for a in word:
        for b in eng_consonants:
            if a == b:
                common_consonants.append(a)

    return common_consonants
