from textblob import TextBlob


class Language:

    '''
    This method tries to automatically detect the language of the word/sentence
    '''

    def autodetect_lang(self, user):

        self.user_input = user.text
        self.word= TextBlob(self.user_input)
        self.current_lang = self.word.detect_language()
        self.total_letters = len(self.user_input.strip())
        self.total_words = len(self.word.words)
        return self.total_result()

    def set_lang(self, user, lang):
        print("Прямое назначение языка")
        self.user_input = user.text
        self.word = TextBlob(self.user_input)
        self.current_lang = lang
        self.total_letters = len(self.user_input.strip())
        self.total_words = len(self.word.words)
        return self.total_result()

    '''
        According to the chosen language of the word, this function sets the suitable alphabet
    '''

    def detect_alphabet(self):

        if self.current_lang == "ru":

            self.alphabet_vowels = ('А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                         'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')

            self.alphabet_consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
                             'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
                             'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П',
                             'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ')

        elif self.current_lang == "en":

            self.alphabet_consonants = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                                    'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
                                    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                                    'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

            self.alphabet_vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')


        elif self.current_lang == "fr":

            self.alphabet_consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                                        'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
                                        'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                                        'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z')

            self.alphabet_vowels = ('a', 'e', 'o', 'u', 'y', 'i', 'A', 'E', 'O', 'U', 'Y', 'I')

    '''
    This function finds all vowels and consonants in the word/sentence.
    '''

    def analyze_consonants(self, word):
        word = list(word)
        consonants = self.alphabet_consonants
        self.consonants = []

        for a in word:
            for b in consonants:
                if a == b:
                    self.consonants.append(a)

        return self.consonants

    def analyze_vowels(self, word):
        word = list(word)
        vowels = self.alphabet_vowels
        self.vowels = []

        for a in word:
            for b in vowels:
                if a == b:
                    self.vowels.append(a)

        return self.vowels

    def total_result(self):

        self.detect_alphabet()



        # This var stores the final message which will be printed for the user.
        self.message_result = ""

        # Separator for different data, e.g. vowels and consonants lists.
        separator = ","

        if len(self.word.words) > 1:

            if self.current_lang == "ru":
                self.message_result += "Вы ввели русское предложение: «" + self.user_input + "»\n"
                self.message_result += "\nИтого слов в предложении: "
                self.message_result += str(self.total_words)
                self.message_result += "\nИтого букв в предложении: "
                self.message_result += str(self.total_letters)
                self.message_result += "\nВсего согласных: "
                self.message_result += separator.join(self.analyze_consonants(self.user_input))
                self.message_result += "\nВсего гласных: "
                self.message_result += separator.join(self.analyze_vowels(self.user_input))

            elif self.current_lang == "en":
                self.message_result += "You've entered an English sentence: «" + self.user_input + "»"
                self.message_result += "\nTotal number of words in the sentence: "
                self.message_result += str(self.total_words)
                self.message_result += "\nTotal number of letters in the sentence: "
                self.message_result += str(self.total_letters)
                self.message_result += "\nTotal number of consonants: "
                self.message_result += "(" + str(len(self.analyze_consonants(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_consonants(self.user_input))
                self.message_result += "\nTotal number of vowels: "
                self.message_result += "(" + str(len(self.analyze_vowels(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_vowels(self.user_input))

            elif self.current_lang == "uz":
                self.message_result += "O'zbek tilidagi «" + self.user_input + "»" + " gapini yozdingiz"

            elif self.current_lang == "fr":
                self.message_result += "Vous avez entré un mot français: «" + self.user_input + "»"
                self.message_result += "\nNombre total de mots dans la phrase: "
                self.message_result += str(self.total_words)
                self.message_result += "\nNombre total de lettres dans le mot: "
                self.message_result += str(self.total_letters)
                self.message_result += "\nNombre total de consonnes: "
                self.message_result += "(" + str(len(self.analyze_consonants(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_consonants(self.user_input))
                self.message_result += "\nNombre total de voyelles: "
                self.message_result += "(" + str(len(self.analyze_vowels(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_vowels(self.user_input))

            elif self.current_lang == "de":
                self.message_result += "Sie haben einen englischen Satz eingegeben: «" + self.user_input + "»"

            else:
                self.message_result += "You've entered a sentence from language (" + self.current_lang + ") which I do not know: «" + self.user_input + "»"

        else:

            if self.current_lang == "ru":
                self.message_result += "Вы ввели русское слово: «" + self.user_input + "»\n"
                self.message_result += "\nИтого букв в слове: "
                self.message_result += str(self.total_letters)
                self.message_result += "\nВсего согласных: "
                self.message_result += "(" + str(len(self.analyze_consonants(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_consonants(self.user_input))
                self.message_result += "\nВсего гласных: "
                self.message_result += "(" + str(len(self.analyze_vowels(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_vowels(self.user_input))

            elif self.current_lang == "en":
                self.message_result += "You've entered an English word: «" + self.user_input + "»"
                self.message_result += "\nTotal number of letters in the word: "
                self.message_result += str(self.total_letters)
                self.message_result += "\nTotal number of consonants: "
                self.message_result += "(" + str(len(self.analyze_consonants(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_consonants(self.user_input))
                self.message_result += "\nTotal number of vowels: "
                self.message_result += "(" + str(len(self.analyze_vowels(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_vowels(self.user_input))

            elif self.current_lang == "uz":
                self.message_result += "O'zbek tilidagi «" + self.user_input + "»" + "so'zini yozdingiz\n"

            elif self.current_lang == "fr":
                self.message_result += "Vous avez entré une phrase français: «" + self.user_input + "»\n"
                self.message_result += "\nNombre total de lettres dans le mot: "
                self.message_result += str(self.total_letters)
                self.message_result += "\nNombre total de consonnes: "
                self.message_result += "(" + str(len(self.analyze_consonants(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_consonants(self.user_input))
                self.message_result += "\nNombre total de voyelles: "
                self.message_result += "(" + str(len(self.analyze_vowels(self.user_input))) + ") "
                self.message_result += separator.join(self.analyze_vowels(self.user_input))

            elif self.current_lang == "de":
                self.message_result += "Sie haben ein deutsches Wort eingegeben: «" + self.user_input + "»\n"

            else:
                self.message_result += "You've entered a word from language (" + self.current_lang + ") which I do not know: «" + self.user_input + "»"

        return self.message_result
