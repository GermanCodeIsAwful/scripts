import pyautogui
import time


def main():
    # Warte 5 Sekunden
    time.sleep(5)

    while True:
        # Führe Strg + V aus (Einfügen)
        pyautogui.hotkey('ctrl', 'v')

        # Drücke Enter
        pyautogui.press('enter')

        # Warte 130 Sekunden
        time.sleep(10)


if __name__ == "__main__":
    main()
    # Telefoniere mit dodo
    # Dodo jetzt uni
