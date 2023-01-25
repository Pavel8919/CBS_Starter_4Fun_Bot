from random import choice
from time import sleep
from pyfiglet import Figlet
import termcolor

COLORS = ['red', 'blue', 'yellow', 'green']


def ascii_art():
    # Getting fonts from module
    fonts_list = Figlet().getFonts()
    # Getting phrase from user for converting
    user_input = input('Фраза для конвертації: ')
    # Setting random font
    Figlet().setFont(font=choice(fonts_list))
    # Setting random color
    set_color = choice(COLORS)
    # Printing result
    termcolor.cprint(Figlet().renderText(user_input), set_color)
    sleep(2)
