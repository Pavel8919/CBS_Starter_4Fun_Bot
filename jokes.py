import pyjokes
from time import sleep


def jokes():
    sleep(1)
    print(pyjokes.get_joke())
    while True:
        print("Бажаєте ще анекдот?")
        choice = str(input('Відповідь (y/n): '))
        if choice == "y":
            sleep(1)
            print(pyjokes.get_joke())
        elif choice == "n":
            sleep(1)
            break
