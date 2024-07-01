from typing import Tuple

import keyboard
import time


def berechne(input_zahl: int, price: int) -> tuple[int, int]:
    anzahl = input_zahl // price
    rest = input_zahl % price
    return anzahl, rest


if __name__ == '__main__':
    div_price: int = 150

    while True:
        try:
            input_c: int = int(input('How many c? : '))

            div, c = berechne(input_c, div_price)
            print(f'{div} div | {c} c')
            print('--------------------')
        except:
            print('\nbye')
            break
