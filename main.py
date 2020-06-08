"""
Automatically pressing the matchmaking 'accept' button
"""
import sys
from time import sleep
import pyautogui
from PIL import Image
from imagehash import average_hash
from fuzzywuzzy import process

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()  # width and height of your screen

button = average_hash(Image.open('button.png'))  # initialise the image of the button
BUTTON_WIDTH = 534  # width of the button of the screen
BUTTON_HEIGHT = 106  # height of the button of the screen

pick_screen = average_hash(Image.open('all_pick.png'))  # initialise the image of the pick screen

CUTOFF = 5  # allowed difference between the initial image of the button and the one on the screen
COOLDOWN = 1  # how often the program checks if the button appeared


def auto_accept():
    """
    Compares a cropped screenshot and the image of the button
    """
    sleep(COOLDOWN)
    screenshot = average_hash(pyautogui.screenshot(region=(SCREEN_WIDTH - (BUTTON_WIDTH / 2),
                                                           SCREEN_HEIGHT - (BUTTON_HEIGHT * 0.7),
                                                           BUTTON_WIDTH,
                                                           BUTTON_HEIGHT)))

    if screenshot - button < CUTOFF:
        print('Found the button')
        pyautogui.click(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    else:
        print('No button found')
        auto_accept()


def auto_ban(hero):
    """
    Bans a hero if you specify one
    """
    sleep(1)
    screenshot2 = average_hash(pyautogui.screenshot(region=(0,
                                                            SCREEN_HEIGHT * 0.33,
                                                            SCREEN_WIDTH * 1.4,
                                                            SCREEN_HEIGHT * 1.15)))

    if screenshot2 - pick_screen < CUTOFF:
        print("Banning " + hero)
        sleep(5)
        pyautogui.typewrite(hero, interval=0.1)
        pyautogui.typewrite(['enter'], interval=0.1)
        pyautogui.click(x=SCREEN_WIDTH * 3 / 3.7, y=SCREEN_HEIGHT * 3 / 4.5)
        print(hero + " banned")
    else:
        print("Banning phase has not started yet")
        auto_ban(hero)


# auto_accept()

if len(sys.argv) > 2:
    with open('heroes.txt', 'r') as heroes_list:
        heroes = heroes_list.readlines()
        choice = process.extractOne(str(sys.argv[1:]), heroes)[0]
    print('You chose to ban', choice)
    auto_ban(choice)
