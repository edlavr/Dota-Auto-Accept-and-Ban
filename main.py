"""
Automatically pressing the matchmaking 'accept' button
"""
from time import sleep
import pyautogui
from PIL import Image
from imagehash import average_hash

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()  # width and height of your screen

button = average_hash(Image.open('button.png'))  # initialise the image of the button
BUTTON_WIDTH = 534  # width of the button of the screen
BUTTON_HEIGHT = 106  # height of the button of the screen

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


auto_accept()
