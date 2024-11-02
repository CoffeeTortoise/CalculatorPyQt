from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


def make_label(label: QLabel, 
               font: QFont,
               text: str,
               pos: tuple[int, int]) -> None:
    label.setFont(font)
    label.setText(text)
    label.move(pos[0], pos[1])
