import sys
import threading

from PyQt6.QtWidgets import QApplication

import hotkey
import engine

from ui import Window




def main():

    app = QApplication(sys.argv)


    # Start F8 listener
    hotkey.start_listener()


    # Start macro engine in background
    engine_thread = threading.Thread(
        target=engine.run,
        daemon=True
    )

    engine_thread.start()



    window = Window()

    window.show()


    sys.exit(
        app.exec()
    )




if __name__ == "__main__":

    main()