from pyfiglet import Figlet
import random


def write_title():
    # select a random title and write
    r = random.randint(0, 9)
    fonts = ['slant', '5lineoblique', 'alligator', 'basic', 'epic', 'isometric1', 'larry3d', 'univers', 'smkeyboard', 'speed']

    f = Figlet(font=fonts[r])
    print(f.renderText('SPM'))
    table_maker("Safe Password Manager")


def table_maker(text):
    # make a table for important textss
    print("_" * (len(text) + 10))
    print("|", " " * 2, text, " " * 2, "|")
    print("-" * (len(text) + 10))
