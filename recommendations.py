from prettytable import PrettyTable
from time import sleep
import random


def interesting_facts():
    facts = [
        "Кожен сьомий у світі китаєць, а кожен пятий у світі псих. Ми живемо у світі де панують китайці й психи!",
        "Чіпси вперше приготували 24 серпня 1853 в якості жартівливої відповіді на скаргу клієнта про те, "
        "що скибочки картоплі занадто товсті та не просмажені.",
        "Чхання може бути неймовірно швидким. Було підраховано, що швидкість чхання становить більш "
        "ніж 160 км на годину.",
        "11% всіх зламаних сканерів виходять з ладу тому, що люди сідають на них для копії частин тіла!",
        "Коли європейці вперше побачили жирафу, вони назвали її «верблюдопардом», вирішивши, що це гібрид "
        "верблюда і леопарда.",
        "Якщо зустрінетеся з восьминогом, загляньте йому в очі, це може бути цікаво: у восьминогів прямокутні зіниці.",
        "Експортна назва автомобіля Лада Калина для Фінляндії — Lada 119, оскільки в перекладі з фінської Kalina "
        "значить тріск, гуркіт, деренчання і стукіт.",
        "Шотландський фізик Роберт Уотсон-Уотт одного разу був зупинений поліціянтом за перевищення швидкості, після "
        "чого сказав: «Якби я знав, що ви будете з ним робити, то ніколи не винайшов би радар!».",
        "У Windows не можна створити файл або теку під назвою «Con», бо у Білла Гейтса в дитинстві було прізвисько, "
        "Con — ботанік. І він постарався щоб в його системі були відсутні такі файли й теки.",
        "На поверхні звичайного офісного столу кількість бактерій в 400 разів більша, ніж на сидінні унітазу.",
        "У 18 столітті серед парижанок було модно носити капелюшки з громовідводами."
        ]
    sleep(1)
    print(facts[random.randint(0, 10)])
    while True:
        print("\nБажаєте ще цікавий факт?")
        choice = str(input('Відповідь (y/n): '))
        if choice == "y":
            sleep(1)
            print(facts[random.randint(0, 10)])
        elif choice == "n":
            sleep(1)
            break
    pass


def recommend_game():
    shooter_list = ['Call of Duty', 'DOOM', 'Counter-Strike']
    action_list = ['PUBG', 'Grand Theft Auto', 'Fortnite']
    strategy_list = ['Age of Empires IV', 'Evil Genius', 'Warhammer']
    games_menu = PrettyTable()
    print('Ви в меню рекомендації ігр. Оберіть жанр гри:')
    games_menu.add_column("Номер жанру", ["1", "2", "3", "4"])
    games_menu.add_column("Жанр гри", ["Шутер", "Екшн", "Стратегія", "Вихід в головне меню"])
    sleep(1)
    print(games_menu)
    sleep(1)
    game_choice = int(input('Введіть обраний номер: '))
    if game_choice == 1:
        print('В обраному жанрі рекомендуємо гру: ', random.choice(shooter_list))
        return_to_main()
    elif game_choice == 2:
        print('В обраному жанрі рекомендуємо гру: ', random.choice(action_list))
        return_to_main()
    elif game_choice == 3:
        print('В обраному жанрі рекомендуємо гру: ', random.choice(strategy_list))
        return_to_main()
    elif game_choice == 4:
        return_to_main()
        pass


def recommend_film():
    horror_list = ['Прокляття', 'Білий шум', 'Туман', '1408', 'Легіон']
    comedy_list = ['Ніч в музеї', 'Третій зайвий', 'Троє в каное', 'Доктор Дуліттл', 'Похмілля у Вегасі']
    action_list = ['Самаритянин', 'Чорний Адам', 'Бладшот', 'Початок', 'Форсаж']
    film_menu = PrettyTable()
    print('Ви в меню рекомендації фільму. Оберіть жанр фільму:')
    film_menu.add_column("Номер жанру", ["1", "2", "3", "4"])
    film_menu.add_column("Жанр фільму", ["Жах", "Комедія", "Бойовик", "Вихід в головне меню"])
    sleep(1)
    print(film_menu)
    sleep(1)
    film_choice = int(input('Введіть обраний номер: '))
    if film_choice == 1:
        print('В обраному жанрі рекомендуємо фільм: ', random.choice(horror_list))
        return_to_main()
    elif film_choice == 2:
        print('В обраному жанрі рекомендуємо фільм: ', random.choice(comedy_list))
        return_to_main()
    elif film_choice == 3:
        print('В обраному жанрі рекомендуємо фільм: ', random.choice(action_list))
        return_to_main()
    elif film_choice == 4:
        return_to_main()
        pass


def return_to_main():
    print("Повернення в головне меню...")
    sleep(2)
