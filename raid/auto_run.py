from pyautogui import pixel, click, position, moveTo
from random import uniform
from keyboard import is_pressed
from time import sleep


class MultiB:
    def __init__(self, pos, rgb, debug=True):
        self.pos = pos
        self.rgb = rgb
        self.c = 0
        self.debug = debug
        print('init done')

    def check_pixel(self):
        print(f'check: {pixel(self.pos[0], self.pos[1])}')
        if pixel(self.pos[0], self.pos[1]) == self.rgb:
            click(x=self.pos[0], y=self.pos[1])
            self.c += 1
            print(self.c)
            moveTo(200, 200)


def get_pos():
    pos = position()
    moveTo(200, 200)
    if pos:
        return pos, pixel(pos[0], pos[1])

    return


if __name__ == '__main__':

    print('rdy?')  # go to replay
    while True:
        if is_pressed('1'):
            sleep(0.5)
            pos, rgb = get_pos()
            print((pos, rgb))
            break

    if not pos:
        exit()

    multi = MultiB(pos, rgb)

    while True:
        sleep(5)

        multi.check_pixel()

        if is_pressed('2'):
            print('see ya')
            break
