from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QApplication
)

from PyQt6.QtCore import (
    Qt,
    QTimer
)

from PyQt6.QtGui import (
    QFont
)

import mouse
import hotkey



POINT_NAMES = {

    "point1": "Dumpling 1",
    "point2": "Dumpling 2",
    "point3": "Dumpling 3",
    "point4": "Auto Upgrade",
    "point5": "Upgrade Start",
    "point6": "Change Dumpling",
    "point7": "Color Detect"

}



# ---------------------------------
# Global theme
# ---------------------------------

STYLE = """

QWidget {

    background-color: #121212;
    color: #eeeeee;
    font-family: "Segoe UI";
    font-size: 14px;

}



QLabel#title {

    font-size: 26px;
    font-weight: 700;

}



QLabel#subtitle {

    color: #a1a1aa;
    font-size: 13px;

}



QFrame#card {

    background-color: #18181b;
    border-radius: 16px;
    border: 1px solid #27272a;

}



QLabel#status {

    font-size: 16px;
    font-weight: 600;

}



QPushButton {

    background-color: #27272a;
    border-radius: 10px;
    padding: 10px;
    border: none;

}



QPushButton:hover {

    background-color: #3f3f46;

}



QPushButton#mainButton {

    color: white;
    font-size: 16px;
    font-weight: 700;
    padding: 14px;

    background:
    qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,

        stop:0 #8b5cf6,
        stop:1 #ec4899
    );

}



QPushButton#mainButton:hover {

    background:
    qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,

        stop:0 #a78bfa,
        stop:1 #f472b6
    );

}



QPushButton#pointButton {

    text-align:left;
    padding-left:15px;

}



"""


class Window(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "Dumpling Macro"
        )


        self.resize(
            520,
            720
        )


        self.setStyleSheet(
            STYLE
        )


        self.build_ui()



    def build_ui(self):


        main_layout = QVBoxLayout()

        main_layout.setSpacing(
            18
        )

        main_layout.setContentsMargins(
            25,
            25,
            25,
            25
        )



        # -------------------------
        # Header
        # -------------------------

        title = QLabel(
            "Dumpling Macro"
        )

        title.setObjectName(
            "title"
        )


        subtitle = QLabel(
            "Automation controller"
        )

        subtitle.setObjectName(
            "subtitle"
        )



        header = QVBoxLayout()

        header.addWidget(
            title
        )

        header.addWidget(
            subtitle
        )


        main_layout.addLayout(
            header
        )



        # -------------------------
        # Control Card
        # -------------------------

        control_card = QFrame()

        control_card.setObjectName(
            "card"
        )


        control_layout = QVBoxLayout()

        control_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )



        self.status = QLabel(
            "🔴 Stopped"
        )

        self.status.setObjectName(
            "status"
        )


        self.toggle_button = QPushButton(
            "Start Macro"
        )


        self.toggle_button.setObjectName(
            "mainButton"
        )


        self.toggle_button.clicked.connect(
            hotkey.toggle
        )



        hint = QLabel(
            "Press F8 to toggle"
        )

        hint.setObjectName(
            "subtitle"
        )



        control_layout.addWidget(
            self.status
        )


        control_layout.addSpacing(
            10
        )


        control_layout.addWidget(
            self.toggle_button
        )


        control_layout.addWidget(
            hint
        )


        control_card.setLayout(
            control_layout
        )


        main_layout.addWidget(
            control_card
        )

        
    def build_ui(self):

        main_layout = QVBoxLayout()

        main_layout.setSpacing(
            18
        )

        main_layout.setContentsMargins(
            25,
            25,
            25,
            25
        )


        # -------------------------
        # Header
        # -------------------------

        title = QLabel(
            "Dumpling Macro"
        )

        title.setObjectName(
            "title"
        )


        subtitle = QLabel(
            "Automation controller"
        )

        subtitle.setObjectName(
            "subtitle"
        )


        header = QVBoxLayout()

        header.addWidget(
            title
        )

        header.addWidget(
            subtitle
        )


        main_layout.addLayout(
            header
        )


        # -------------------------
        # Control Card
        # -------------------------

        control_card = QFrame()

        control_card.setObjectName(
            "card"
        )


        control_layout = QVBoxLayout()

        control_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        self.status = QLabel(
            "🔴 Stopped"
        )

        self.status.setObjectName(
            "status"
        )


        self.toggle_button = QPushButton(
            "Start Macro"
        )

        self.toggle_button.setObjectName(
            "mainButton"
        )


        self.toggle_button.clicked.connect(
            hotkey.toggle
        )


        hint = QLabel(
            "F8 shortcut • Manual control available"
        )

        hint.setObjectName(
            "subtitle"
        )


        control_layout.addWidget(
            self.status
        )

        control_layout.addSpacing(
            10
        )

        control_layout.addWidget(
            self.toggle_button
        )

        control_layout.addWidget(
            hint
        )


        control_card.setLayout(
            control_layout
        )


        main_layout.addWidget(
            control_card
        )



        # -------------------------
        # Coordinate Card
        # -------------------------

        points_card = QFrame()

        points_card.setObjectName(
            "card"
        )


        points_layout = QVBoxLayout()

        points_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        points_title = QLabel(
            "Coordinate Setup"
        )

        points_title.setFont(
            QFont(
                "Segoe UI",
                15,
                QFont.Weight.Bold
            )
        )


        points_layout.addWidget(
            points_title
        )


        points_layout.addSpacing(
            10
        )


        self.buttons = {}



        for point, name in POINT_NAMES.items():


            button = QPushButton()


            button.setObjectName(
                "pointButton"
            )


            button.clicked.connect(
                lambda checked,
                p=point:
                self.set_point(p)
            )


            self.buttons[point] = button


            points_layout.addWidget(
                button
            )



        points_card.setLayout(
            points_layout
        )


        main_layout.addWidget(
            points_card
        )



        # -------------------------
        # Footer
        # -------------------------

        footer = QLabel(
            "Dumpling Macro • Ready"
        )

        footer.setObjectName(
            "subtitle"
        )


        footer.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        main_layout.addWidget(
            footer
        )



        self.setLayout(
            main_layout
        )


        # Hotkey status callback

        hotkey.add_callback(
            self.update_status
        )


        # Refresh timer

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.refresh_status
        )

        self.timer.start(
            200
        )


        self.update_point_labels()





    # ---------------------------------
    # Point setup
    # ---------------------------------

    def set_point(self, point_name):

        name = POINT_NAMES[point_name]


        self.buttons[point_name].setText(
            f"Click screen for {name}"
        )


        mouse.capture_point(
            point_name,
            self.point_saved
        )





    def point_saved(self, name, coords):

        display = POINT_NAMES[name]


        self.buttons[name].setText(
            f"{display}\n{coords[0]}, {coords[1]}"
        )





    def update_point_labels(self):

        for point, coords in mouse.POINTS.items():


            name = POINT_NAMES[point]


            if coords is None:


                self.buttons[point].setText(
                    f"{name}\nNot Set"
                )


            else:


                self.buttons[point].setText(
                    f"{name}\n{coords[0]}, {coords[1]}"
                )





    # ---------------------------------
    # Status handling
    # ---------------------------------

    def refresh_status(self):

        self.update_status(
            hotkey.is_running()
        )





    def update_status(self, running):

        if running:


            self.status.setText(
                "🟢 Running"
            )


            self.toggle_button.setText(
                "Stop Macro"
            )



        else:


            self.status.setText(
                "🔴 Stopped"
            )


            self.toggle_button.setText(
                "Start Macro"
            )