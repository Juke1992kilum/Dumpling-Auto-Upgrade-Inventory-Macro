import time
import json
import os

from PIL import ImageGrab
from pynput import mouse as pynput_mouse


# ---------------------------------
# Settings file
# ---------------------------------

SETTINGS_FILE = "settings.json"



DEFAULT_SETTINGS = {

    "points": {
        "point1": None,
        "point2": None,
        "point3": None,
        "point4": None,
        "point5": None,
        "point6": None,
        "point7": None
    },

    "timings": {

        # 100 milliseconds
        "timing_1": 0.1,

        # 50 milliseconds
        "timing_2": 0.05,

        # 8 minutes
        "timing_3": 480,

        # Delay between sprites
        "sprite_switch_delay": 5
    }
}



# ---------------------------------
# Load / Save settings
# ---------------------------------

def save_settings(data):

    with open(
        SETTINGS_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



def load_settings():

    if not os.path.exists(
        SETTINGS_FILE
    ):

        save_settings(
            DEFAULT_SETTINGS
        )

        return DEFAULT_SETTINGS



    with open(
        SETTINGS_FILE,
        "r"
    ) as file:

        return json.load(file)




SETTINGS = load_settings()



# ---------------------------------
# Coordinates
# ---------------------------------

POINTS = SETTINGS["points"]



# ---------------------------------
# Timings
# ---------------------------------

TIMING_1 = SETTINGS["timings"]["timing_1"]

TIMING_2 = SETTINGS["timings"]["timing_2"]

TIMING_3 = SETTINGS["timings"]["timing_3"]

SPRITE_SWITCH_DELAY = (
    SETTINGS["timings"]["sprite_switch_delay"]
)



# ---------------------------------
# Mouse controller
# ---------------------------------

_controller = pynput_mouse.Controller()



# ---------------------------------
# Movement
# ---------------------------------

def move_to(point_name):
    """
    Move mouse to saved coordinate.
    """

    position = POINTS.get(
        point_name
    )


    if position is None:

        print(
            f"{point_name} is not set"
        )

        return False



    _controller.position = (
        position[0],
        position[1]
    )


    return True




def click():
    """
    Left click current mouse position.
    """

    _controller.click(
        pynput_mouse.Button.left
    )




def scroll_down(amount=2):
    """
    Scroll downward.
    """

    _controller.scroll(
        0,
        -amount
    )




# ---------------------------------
# Coordinate capture
# ---------------------------------

def capture_point(point_name, callback=None):
    """
    Wait for user to click screen.
    Save coordinate.
    """


    def on_click(x, y, button, pressed):

        if pressed:


            POINTS[point_name] = [
                x,
                y
            ]


            SETTINGS["points"] = POINTS


            save_settings(
                SETTINGS
            )


            print(
                f"{point_name}: {(x,y)}"
            )



            if callback:

                callback(
                    point_name,
                    (x, y)
                )


            return False



    listener = pynput_mouse.Listener(
        on_click=on_click
    )


    listener.start()




# ---------------------------------
# Timing
# ---------------------------------

def wait_short():

    time.sleep(
        TIMING_1
    )




def wait_medium():

    time.sleep(
        TIMING_2
    )




def wait_sprite_switch():

    time.sleep(
        SPRITE_SWITCH_DELAY
    )




def wait_interruptible(seconds, running_check):
    """
    Long wait that can be stopped with F8.
    """

    elapsed = 0


    while elapsed < seconds:


        if not running_check():

            return False



        time.sleep(
            0.1
        )


        elapsed += 0.1



    return True




# ---------------------------------
# Color detection
# ---------------------------------

def get_pixel(point_name):

    position = POINTS.get(
        point_name
    )


    if position is None:

        return None



    screenshot = ImageGrab.grab()



    return screenshot.getpixel(
        (
            position[0],
            position[1]
        )
    )




def is_orange(point_name="point7"):
    """
    Checks for exact color:

    Hex:
        #ffcd70

    RGB:
        255,205,112
    """


    pixel = get_pixel(
        point_name
    )


    if pixel is None:

        return False



    r, g, b = pixel[:3]



    return (
        r == 255
        and
        g == 205
        and
        b == 112
    )