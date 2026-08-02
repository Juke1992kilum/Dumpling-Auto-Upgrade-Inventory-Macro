import time

import mouse
import hotkey

SPRITE_SWITCH_DELAY = 5

def wait_sprite_switch():
    """
    Delay between finishing one sprite
    and starting the next one.
    """

    time.sleep(
        SPRITE_SWITCH_DELAY
    )

def spam_click(duration=5, interval=0.01):
    """
    Spam click current mouse location.

    5 seconds total
    10ms between clicks
    """

    start = time.time()


    while time.time() - start < duration:

        if not hotkey.is_running():
            return False


        mouse.click()


        time.sleep(
            interval
        )


    return True





def run_sprite(sprite_point):
    """
    Runs one sprite sequence.

    Sprite
    -> Auto
    -> Established
    -> Color check

    Orange:
        Change

    No orange:
        wait 8 minutes
        Change
        spam click Change
    """



    if not hotkey.is_running():
        return False



    # -------------------------
    # Sprite
    # -------------------------

    mouse.move_to(
        sprite_point
    )

    mouse.click()

    mouse.wait_short()



    # -------------------------
    # Auto
    # -------------------------

    mouse.move_to(
        "point4"
    )

    mouse.click()

    mouse.wait_short()



    # -------------------------
    # Established
    # -------------------------

    mouse.move_to(
        "point5"
    )

    mouse.click()

    mouse.wait_medium()



    # -------------------------
    # Color detection
    # -------------------------

    mouse.move_to(
        "point7"
    )

    mouse.click()



    if not hotkey.is_running():
        return False



    # -------------------------
    # Orange detected
    # -------------------------

    if mouse.is_orange("point7"):

        mouse.move_to(
            "point6"
        )

        mouse.click()


        # Spam click Point 6
        spam_click(
            duration=5,
            interval=0.01
        )



    # -------------------------
    # Orange not detected
    # -------------------------

    else:

        finished = mouse.wait_interruptible(
            mouse.TIMING_3,
            hotkey.is_running
        )


        if not finished:
            return False



        # Move to Change
        mouse.move_to(
            "point6"
        )

        mouse.click()



        # Spam click Point 6
        spam_click(
            duration=5,
            interval=0.01
        )



    wait_sprite_switch()
    return True





def run():
    """
    Main macro loop.
    """

    while True:


        # Wait for F8

        while not hotkey.is_running():

            time.sleep(0.1)



        # =========================
        # Forward order
        # =========================

        run_sprite("point1")

        run_sprite("point2")

        run_sprite("point3")



        if not hotkey.is_running():
            continue



        # Move to Point 1 before scrolling

        mouse.move_to(
            "point1"
        )


        mouse.wait_short()



        # Scroll down 2 ticks

        mouse.scroll_down(
            2
        )


        mouse.wait_short()



        # =========================
        # Reverse order
        # =========================

        run_sprite("point3")

        run_sprite("point2")

        run_sprite("point1")



        if not hotkey.is_running():
            continue



        # Move to Point 1 before scrolling again

        mouse.move_to(
            "point1"
        )


        mouse.wait_short()



        # Scroll down 2 ticks

        mouse.scroll_down(
            2
        )


        mouse.wait_short()