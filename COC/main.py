import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from random import uniform
import pytesseract
import keyboard
import winsound
import time


class AutoSearch:
    CONFIG = 'outputbase digits'  # r'--oem 3 --psm 6'
    TESSERACT_PATH = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    def __init__(self, coord, min_currency, continue_coord, debug):
        pytesseract.pytesseract.tesseract_cmd = self.TESSERACT_PATH
        self.bbox = coord
        self.min_currency = min_currency
        self.debug = debug
        self.continue_coord = continue_coord

        print('starting...')

    def _get_values(self):
        screenshot = np.array(ImageGrab.grab(self.bbox))

        screenshot_hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

        mask_gold = cv2.inRange(screenshot_hsv, np.array([27, 0, 200]), np.array([33, 100, 255]))
        mask_elix = cv2.inRange(screenshot_hsv, np.array([149, 0, 200]), np.array([156, 100, 255]))

        try:
            detected_gold = int(pytesseract.image_to_string(mask_gold, config=self.CONFIG))
            detected_elix = int(pytesseract.image_to_string(mask_elix, config=self.CONFIG))
        except Exception:
            if self.debug:
                print('skip???')
            return 0, 0

        if self.debug:
            print(f'g:{detected_gold:,}+e:{detected_elix:,}={(detected_gold + detected_elix):,}')

            # cv2.imshow('Screenshot', cv2.bitwise_or(mask_gold, mask_elix))
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

        return detected_gold, detected_elix

    def start_process(self):
        while True:
            if keyboard.is_pressed('q'):
                print('break in process')
                break

            gold, elix = self._get_values()

            if self.min_currency <= (gold + elix) <= 3500000:
                print(f'LOOOOOOOOOOOT')
                winsound.Beep(400, 1000)
                break

            pyautogui.leftClick(uniform(self.continue_coord[0] - 100, self.continue_coord[0] + 100),
                                uniform(self.continue_coord[1] - 50, self.continue_coord[1] + 50))
            time.sleep(uniform(2, 5))

    def wrong_next(self):
        pyautogui.leftClick(uniform(self.continue_coord[0] - 100, self.continue_coord[0] + 100),
                            uniform(self.continue_coord[1] - 50, self.continue_coord[1] + 50))
        time.sleep(uniform(2, 5))


if __name__ == '__main__':
    # Python console: import pyautogui; pyautogui.position()
    auto_search = AutoSearch((80, 125, 235, 200), 1500000, (1730, 800), debug=True)
    #auto_search.start_process()

    while True:
        time.sleep(1)

        if keyboard.is_pressed('u'):
            print('see ya')
            break

        if keyboard.is_pressed('w'):
            print('letssss go')
            auto_search.start_process()

        if keyboard.is_pressed('e'):
            print('Wrong stop, go to the next one')
            auto_search.wrong_next()
            auto_search.start_process()
