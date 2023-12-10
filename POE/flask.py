from pyautogui import pixel, press, position
from random import uniform
from keyboard import is_pressed
from time import sleep


class DoFlask:
    def __init__(self, pos, rgb):
        self.pos = pos
        self.rgb = rgb

    def start(self):
        count = 0
        gradegefunden = 0
        print('lets go')
        while True:
            if not pixel(self.pos[0], self.pos[1]) == self.rgb:
                press('1')
                count += 1
                gradegefunden += 1
            else:
                gradegefunden = 0

            if gradegefunden == 2:
                sleep(uniform(1, 2))

            sleep(uniform(0.001, 0.1))

            if is_pressed('q'):
                print(f'{count} mal den kack gedrückt')
                print('break')
                break




def get_pos():
    pos = position()

    if pos:
        return pos, pixel(pos[0], pos[1])

    return


if __name__ == '__main__':

    input('rdy?')
    pos, rgb = get_pos()

    if not pos:
        exit()

    do_flask = DoFlask(pos, rgb)

    while True:
        sleep(0.5)

        if is_pressed('w'):
            do_flask.start()

        if is_pressed('r'):
            print('see ya')
            break
