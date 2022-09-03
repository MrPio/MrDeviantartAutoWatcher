import time
from types import NoneType

import pyautogui
from pyautogui import moveTo,scroll,sleep,click,hotkey,locateOnScreen


def wait_for_element_appear(element_path: str, wait=8.0, confidence=0.7, grayscale=False):
    start = time.time()
    while True:
        element = locateOnScreen(element_path, grayscale=grayscale, confidence=confidence)
        if time.time() - start > wait:
            # print(f"I've waited too much! [{element_path}]")
            return None
        sleep(0.5)
        if type(element) is not NoneType:
            break
    return element


def click_center(element):
    click(x=element.left + int(element.width / 2),
                    y=element.top + int(element.height / 2))

def position_mouse(element):
    moveTo(x=element.left + int(element.width / 2),
                    y=element.top + int(element.height / 2))



def auto_watcher():

    # open the tab that shows all the account who facourited that post
    star = wait_for_element_appear('ui\\star.png', 6, confidence=0.98)
    click_center(star)

    # watch all the accounts scrolling down when no '+ watch' is found
    for i in range(999):
        watch = wait_for_element_appear('ui\\+watch.png', 3, confidence=0.9)

        # '+ watch' cannot be found, so I scroll down
        if (type(watch) == NoneType):
            watching = wait_for_element_appear('ui\\+watching.png', 2, confidence=0.8)
            if (type(watching) == NoneType):
                hotkey('alt','left')
                sleep(2)
                break
            position_mouse(watching)
            print('scrolling')
            scroll(-240)
            sleep(0.5)
            continue

        click_center(watch)
        print('watched!')
        sleep(0.5)

    auto_watcher()

def auto_feature():
    pyautogui.sleep(4)
    pyautogui.PAUSE=0.02
    for i in range(999):
        for i in range(6):
            pyautogui.press('tab')
            # pyautogui.sleep(0.01)
        pyautogui.press('space')
        pyautogui.sleep(0.15)

if __name__ == '__main__':
    auto_feature()