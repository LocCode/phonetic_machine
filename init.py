

def init():
    print("\n----------")
    print("\nDeveloper: Malik Khodjaev / Разработчик: Малик Ходжаев")
    print("\n----------")
    print("\nHello. To choose English just type: eng")
    print("\nIf you want to exit just type: exit")
    print("\nПривет. Чтобы выбрать русский язык введи: рус")
    print("\nЧтобы выйти из программы введи: выйти")
    print("\n----------")

    lang = input()

    if lang == "eng" or lang == "рус":

        choose_lang(lang)

    elif lang == "exit" or lang == "выйти":
        "\nBye! Пока!"
        exit()

    else:

        print("\nJust enter eng to use English. Otherwise the program will be closed.")
        print("\nПросто введите рус, чтобы использовать русский язык. Иначе программа будет закрыта.")


def eng_language():

    from phonetic_machine import engFunc

    print("\nOK. You have chosen English.")
    print("Now you can enter any word in English and we will make a phonetic analysis of it.")

    word = input()

    # Отправляем слово на проверку
    word_result = engFunc.get_english_word(word)

    # Выводим результаты фонетического анализа слова
    print("\nThe result of phonetic analysis of the word «", word, "»")

    # Вывод количества букв в вводимом слове
    print("\nTotal letters in the «", word, "»:", word_result[0])

    # Вывод количества гласных и их количества
    print("\nTotal consonants in the word «", word, "»:", len(word_result[1]))
    print("The list of consonants of the word: «", word, "»:", word_result[1])

    # Вывод количества согласных и их количества
    print("\nTotal vowels in the word «", word, "»:", len(word_result[2]))
    print("The list of vowels of the word: «", word, "»:", word_result[2])

    print("\n Do you want to enter another word? (yes/no)?")

    if input() == "yes":

        eng_language()

    elif input() == "no":

        print("See you soon! Увидемся!")
        exit()

    else:
        print("Just enter yes or no, nothing more. Otherwise the program will be closed.")
        input()


def ru_language():
    from phonetic_machine import ruFunc

    print("\nХорошо. Вы выбрали русский язык.")
    print("Теперь вы можете ввести любое слово по-русски и мы сделаем их фонетический анализ.")

    word = input()

    # Отправляем слово на проверку
    word_result = ruFunc.get_russian_word(word)

    # Выводим результаты фонетического анализа слова
    print("\nРезультат фонетического анализа слова «", word, "»")

    # Вывод количества букв в вводимом слове
    print("\nВсего букв в слове «", word, "»:", word_result[0])

    # Вывод количества гласных и их количества
    print("\nВсего гласных в слове «", word, "»:", len(word_result[1]))
    print("Список гласных в слове: «", word, "»:", word_result[1])

    # Вывод количества согласных и их количества
    print("\nВсего согласных в слове «", word, "»:", len(word_result[2]))
    print("Список согласных в слове: «", word, "»:", word_result[2])

    print("\n Вы хотите ввести другое слово? (да/нет)?")

    if input() == "да":

        ru_language()

    elif input() == "нет":

        print("See you soon! Увидемся!")
        exit()

    else:
        print("Просто введите да или нет, ничего более. Иначе программа будет закрыта.")
        input()


def choose_lang(lang):

    if lang == "eng":

        eng_language()

    elif lang == "рус":

        ru_language()

    elif lang == "exit" or lang == "выйти":
        print("See you soon! Увидемся!")
        exit()


# [/] Запуск системы
init()
# Запуск системы [/]
