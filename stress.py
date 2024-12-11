import random


class Quiz:
    def __init__(self, question: str, options: list[str], correct_number: int):
        self.question = question
        self.options = options
        self.correct_number = correct_number

    def shuffle_options(self):
        correct_word = self.options[self.correct_number]
        random.shuffle(self.options)

        for num, word in enumerate(self.options):
            if word == correct_word:
                self.correct_number = num
                break

    def get(self):
        self.shuffle_options()
        return self


quiz_list: list = list()

with open('words.txt', 'r', encoding='utf-8') as file:
    for line in file.read().splitlines():
        temp = line.split('|')
        word = temp[0]

        options = list()
        correct_number = 0
        for num, variant in enumerate(temp[1].split()):
            if '.' in variant:
                correct_number = num
                variant = variant.rstrip('.')

            options.append(variant)

        quiz_list.append(Quiz(word, options, correct_number))


def get_random_quiz():
    return random.choice(quiz_list).get()
