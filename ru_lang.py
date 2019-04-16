# Списки гласных и согласных букв в русском языке
ru_vowels = ('А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
              'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
ru_consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
                  'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
                  'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П',
                  'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ')


# Получаем вводимое пользователем слово
def get_russian_word(word):
    letters = len(word)
    vowels = count_vowels(word)
    consonants = count_consonants(word)
    # Возвращаем результат пользователю
    return letters, vowels, consonants


"""Подсчитываем количество гласных в слове"""


def count_vowels(word):
    word = list(word)
    common_vowels = []
    for a in word:
        for b in ru_vowels:
            if a == b:
                common_vowels.append(a)
    return common_vowels


"""Подсчитываем количество согласные в слове"""


def count_consonants(word):
    word = list(word)
    common_consonants = []
    for a in word:
        for b in ru_consonants:
            if a == b:
                common_consonants.append(a)
    return common_consonants
