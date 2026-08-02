from pynput import keyboard


running = False


_callbacks = []



def toggle():

    global running

    running = not running

    print(
        "Running"
        if running
        else
        "Stopped"
    )


    for callback in _callbacks:
        callback(running)



def is_running():

    return running



def add_callback(callback):

    _callbacks.append(callback)



def start_listener():

    listener = keyboard.Listener(
        on_press=on_press
    )

    listener.daemon = True
    listener.start()



def on_press(key):

    try:

        if key == keyboard.Key.f8:
            toggle()

    except Exception:

        pass