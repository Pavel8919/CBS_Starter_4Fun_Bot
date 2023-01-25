from games import *
from recommendations import *
from jokes import *
from ascii_art import *


def main():
    print('Вас вітає розважальний чат-бот!')
    while True:
        table_menu = PrettyTable()
        print('Ви в головному меню. Оберіть номер розваги:')
        table_menu.add_column("Номер", ["1", "2", "3", "4", "5", "6", "7"])
        table_menu.add_column("Розваги", ["Ігри", "Анекдот", "Цікаві факти", "Рекомендувати гру",
                                          "Рекомендувати фільм", "ASCII ART", "Вихід"])
        print(table_menu)
        sleep(1)
        choice = int(input('Введіть обраний номер: '))
        sleep(1)
        if choice == 1:
            while True:
                games_menu = PrettyTable()
                print('Ви в меню ігр. Оберіть гру:')
                games_menu.add_column("Номер", ["1", "2", "3", "4"])
                games_menu.add_column("Розваги", ["Камінь-ножиці-папір", "Вгадай число", "Поле чудес",
                                                  "Вихід в головне меню"])
                print(games_menu)
                sleep(1)
                game_choice = int(input('Введіть обраний номер: '))
                if game_choice == 1:
                    rock_paper_scissors()
                elif game_choice == 2:
                    guess_number()
                elif game_choice == 3:
                    guess_word()
                elif game_choice == 4:
                    break
        elif choice == 2:
            jokes()
        elif choice == 3:
            interesting_facts()
        elif choice == 4:
            recommend_game()
        elif choice == 5:
            recommend_film()
        elif choice == 6:
            ascii_art()
        elif choice == 7:
            print("Робота чат-бота завершена! До зустрічі!")
            break


if __name__ == '__main__':
    main()
