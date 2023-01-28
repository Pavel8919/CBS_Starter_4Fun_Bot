from prettytable import PrettyTable
from time import sleep
from termcolor import cprint
import random


def rock_paper_scissors():
    choices = ["камінь", "ножиці", "папір", "вихід"]
    rock_paper_scissors_menu = PrettyTable()
    rock_paper_scissors_menu.add_column("Номер", ["1", "2", "3", "4"])
    rock_paper_scissors_menu.add_column("Ваш вибір", ["камінь", "ножиці", "папір", "вихід"])
    player_choice = None
    while player_choice != "4":
        print(rock_paper_scissors_menu)
        player = None
        player_choice = int(input('Введіть обраний номер: '))
        if player_choice == 1:
            player = "камінь"
        elif player_choice == 2:
            player = "ножиці"
        elif player_choice == 3:
            player = "папір"
        elif player_choice == 4:
            break
        computer = choices[random.randint(0, 2)]
        print("Твій вибір " + player + ", комп'ютер обрав " + computer + ".")
        if player == computer:
            cprint("Нічия!", 'yellow', 'on_blue')
        elif player == "камінь":
            if computer == "ножиці":
                cprint("Вітаю! Ти переміг!", 'green')
            else:
                cprint("Переміг комп'ютер!", 'red')
        elif player == "папір":
            if computer == "камінь":
                cprint("Вітаю! Ти переміг!", 'green')
            else:
                cprint("Переміг комп'ютер!", 'red')
        elif player == "ножиці":
            if computer == "папір":
                cprint("Вітаю! Ти переміг!", 'green')
            else:
                cprint("Переміг комп'ютер!", 'red')


def guess_number():
    num_to_guess = random.randint(0, 101)
    print("Загадане число знаходиться в діапазоні від 0 до 100. Вгадайте його!")
    num = int(input())
    counter1 = 1
    while num != num_to_guess:
        if num > num_to_guess:
            num = int(input("Загадане число менше! Спробуйте вгадати ще раз:"))
            counter1 += 1
        else:
            num = int(input("Загадане число більше! Спробуйте вгадати ще раз:"))
            counter1 += 1
    print(f"Вітаю з перемогою! Ви вгадали число з {counter1} спроби!")


def guess_word():
    words = ('КОРИДОР', 'ПОДАРУНОК', 'ЯБЛУКО', 'МАГАЗИН', 'ЗАГАДКА')
    num_chances_to_guess = 10
    sleep(1)
    word_to_guess = random.choice(words)
    word_hidden = '*' * len(word_to_guess)
    print('Загадане слово має наступний вигляд: ', word_hidden)
    sleep(1)
    while (num_chances_to_guess != 0) and (word_hidden != word_to_guess):
        new = ''
        char_guess = input('Введіть літеру, яка, на Вашу думку, міститься в слові: ')
        sleep(1)
        if char_guess != '':
            if char_guess.upper() in word_to_guess:
                for i in range(len(word_to_guess)):
                    if char_guess.upper() == word_to_guess[i]:
                        new += char_guess.upper()
                    else:
                        new += word_hidden[i]
                word_hidden = new
                if word_to_guess == word_hidden:
                    print(f'\nВи виграли!!! Cлово {word_hidden} повністю розгадано!')
                else:
                    print('\nВірна літера! Поточний вигляд слова: ', word_hidden)
            else:
                num_chances_to_guess -= 1
                if num_chances_to_guess == 0:
                    print("Ви програли!")
                else:
                    print(f'\nТакої літери в слові немає, залишилось {num_chances_to_guess} спроб!')
        else:
            print('Помилка вводу, спробуйте знову!')
