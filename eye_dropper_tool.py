import pynput
from PIL import ImageGrab

MOUSE_BUTTONS = pynput.mouse.Button

RECORD_COLOUR_BUTTONS = (MOUSE_BUTTONS.left, MOUSE_BUTTONS.right)

EXIT_BUTTON = MOUSE_BUTTONS.middle


def on_mouse_click(x, y, button, pressed):
    if (
        pressed == True
    ):  # continue only when the button is pressed and not when released
        if button == EXIT_BUTTON:
            MOUSE_LISTENER.stop()
        if button in RECORD_COLOUR_BUTTONS:
            pixel = ImageGrab.grab((x, y, x + 1, y + 1))
            pixel_colour = pixel.getpixel((0, 0))
            print(
                "Pixel Coordinates = ({}, {}) ; RGB value = {}".format(
                    x, y, pixel_colour
                )
            )


MOUSE_LISTENER = pynput.mouse.Listener(on_click=on_mouse_click)
MOUSE_LISTENER.start()
MOUSE_LISTENER.join()
