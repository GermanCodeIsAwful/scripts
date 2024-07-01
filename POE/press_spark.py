import keyboard
import time

def toggle_r():
    global r_pressed
    r_pressed = not r_pressed
    print(r_pressed)
    if r_pressed:
        keyboard.press('r')
    else:
        keyboard.release('r')
    time.sleep(0.2)

r_pressed = False

if __name__ == '__main__':
    try:
        while True:
            time.sleep(0.1)  # Um die CPU-Last zu reduzieren, kurz warten
            if keyboard.is_pressed('ö'):
                toggle_r()
    except KeyboardInterrupt:
        if r_pressed:
            keyboard.release('r')
