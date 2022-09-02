import time
from types import NoneType

import pyautogui


def wait_for_element_appear(element_path: str, wait=8.0, confidence=0.7, grayscale=False):
    start = time.time()
    while True:
        element = pyautogui.locateOnScreen(element_path, grayscale=grayscale, confidence=confidence)
        if time.time() - start > wait:
            print(f"I've waited too much! [{element_path}]")
            return None
        pyautogui.sleep(0.5)
        if type(element) is not NoneType:
            break
    return element


def click_center(element):
    pyautogui.click(x=element.left + int(element.width / 2),
                    y=element.top + int(element.height / 2))

def position_mouse(element):
    pyautogui.moveTo(x=element.left + int(element.width / 2),
                    y=element.top + int(element.height / 2))



def click_first_found(el_list: [], wait: float, confidence=0.9, grayscale=False):
    for el in el_list:
        element = wait_for_element_appear(el, wait=wait, confidence=confidence, grayscale=grayscale)
        if type(element) is not NoneType:
            click_center(element)
            return


def main():

    # open the tab that shows all the account who facourited that post
    star = wait_for_element_appear('ui\\star.png', 6, confidence=0.98)
    click_center(star)

    # watch all the accounts scrolling down when no '+ watch' is found
    for i in range(999):
        watch = wait_for_element_appear('ui\\+watch.png', 1, confidence=0.9)

        # '+ watch' cannot be found, so I scroll down
        if (type(watch) == NoneType):
            watching = wait_for_element_appear('ui\\+watching.png', 2, confidence=0.9)
            if (type(watching) == NoneType):
                pyautogui.hotkey('alt','left')
                pyautogui.sleep(2)
                break
            position_mouse(watching)
            pyautogui.scroll(-240)
            pyautogui.sleep(0.5)
            continue

        click_center(watch)
        pyautogui.sleep(0.5)

    main()

if __name__ == '__main__':
    main()