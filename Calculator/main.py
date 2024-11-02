from config import*
from math import sqrt, pow, sin, cos, tan, acos, asin, atan, exp, log, acosh, asinh, atanh, cosh, sinh, tanh, degrees, radians, factorial, fabs, pi, tau, e
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton
from makefuncs import*


def load_str(path: str) -> str:
    with open(path, 'r') as file:
        value: str = file.read()
    return value


class Calculator:
    def __init__(self) -> None:
        # Window
        self.window: QWidget = QWidget()
        self.window.setWindowTitle(TITLE)
        self.window.setGeometry(SHIFT_X, SHIFT_Y, WND_WIDTH, WND_HEIGHT)
        self.window.setFixedSize(WND_WIDTH, WND_HEIGHT)
        icon: QIcon = QIcon(ICON_PATH)
        self.window.setWindowIcon(icon)

        # Font
        font: QFont = QFont()
        font.setFamily(FONT_PATH)
        font.setPointSize(FNT_SIZE)

        # Label help
        help_txt: str = load_str(FILE_HELP)
        self.help: QLabel = QLabel(self.window)
        help_pos: tuple[int, int] = SIZE, SIZE
        make_label(self.help, font, help_txt, help_pos)

        # Label expression
        expr_txt: str = 'Expression: '
        self.expr: QLabel = QLabel(self.window)
        expr_pos: tuple[int, int] = SIZE, SIZE * 17
        make_label(self.expr, font, expr_txt, expr_pos)
        self.expr.setFrameShape(QLabel.Panel)
        self.expr.setFrameShadow(QLabel.Sunken)

        # Label error
        self.err_txt: str = 'There will be an error message'
        self.err: QLabel = QLabel(self.window)
        err_pos: tuple[int, int] = SIZE * 5, SIZE * 25
        make_label(self.err, font, self.err_txt, err_pos)
        self.c_val: str = 'Check values'
        self.c_type: str = 'Check values type'
        self.c_flow: str = 'Too big value'
        self.c_div: str = 'Division by zero'
        self.c_expres: str = 'Check the expression'

        # Line input
        self.input_line: QLineEdit = QLineEdit(self.window)
        self.input_line.setFont(font)
        line_w: int = SIZE * 26
        line_pos: tuple[int, int] = SIZE * 7, SIZE * 17
        self.input_line.setFixedWidth(line_w)
        self.input_line.move(line_pos[0], line_pos[1])
        self.user_txt: str = ''
        self.default_txt: str = '1 + 1'

        # Button calculate
        self.button: QPushButton = QPushButton(self.window)
        button_txt: str = 'Calculate'
        self.button.setText(button_txt)
        self.button.setFont(font)
        button_pos: tuple[int, int] = SIZE, SIZE * 20
        self.button.clicked.connect(self.calculate)
        self.button.move(button_pos[0], button_pos[1])
        self.answer: str = 'Answer'

        # Button clear
        self.btn_clear: QPushButton = QPushButton(self.window)
        clear_txt: str = 'Clear'
        self.btn_clear.setText(clear_txt)
        self.btn_clear.setFont(font)
        clear_pos: tuple[int, int] = SIZE, SIZE * 23
        self.btn_clear.clicked.connect(self.clear)
        self.btn_clear.move(clear_pos[0], clear_pos[1])

        # Button quit
        self.btn_quit: QPushButton = QPushButton(self.window)
        qt_txt: str = 'Quit'
        self.btn_quit.setText(qt_txt)
        self.btn_quit.setFont(font)
        qt_pos: tuple[int, int] = WND_WIDTH - SIZE * 5, SIZE * 23
        self.btn_quit.clicked.connect(self.quit)
        self.btn_quit.move(qt_pos[0], qt_pos[1])


        # Label answer
        self.lbl_answer: QLabel = QLabel(self.window)
        answ_pos: tuple[int, int] = SIZE * 5, SIZE * 20
        answ_w: int = SIZE * 27
        make_label(self.lbl_answer, font, self.answer, answ_pos)
        self.lbl_answer.setFixedWidth(answ_w)
        self.lbl_answer.setFrameShape(QLabel.Panel)
        self.lbl_answer.setFrameShadow(QLabel.Sunken)

    def calculate(self) -> None:
        self.err.setText(self.err_txt)
        input_txt: str = self.input_line.text()
        txt1: str = input_txt.replace(' ', '')
        txt2: str = txt1.replace('\r', '')
        txt3: str = txt2.replace('\n', '')
        txt4: str = txt3.replace('=', '')
        self.user_txt = txt4
        if len(self.user_txt) < 2:
            self.user_txt = self.default_txt
        try:
            res: float = eval(self.user_txt)
        except NameError:
            res: float = eval(self.default_txt)
            self.err.setText(self.c_expres)
        except SyntaxError:
            res: float = eval(self.default_txt)
            self.err.setText(self.c_expres)
        except ValueError:
            res: float = eval(self.default_txt)
            self.err.setText(self.c_val)
        except TypeError:
            res: float = eval(self.default_txt)
            self.err.setText(self.c_type)
        except OverflowError:
            res: float = eval(self.default_txt)
            self.err.setText(self.c_flow)
        except ZeroDivisionError:
            res: float = eval(self.default_txt)
            self.err.setText(self.c_div)
        try:
            self.answer = str(res)
            self.lbl_answer.setText(self.answer)
        except ValueError:
            res: float = eval(self.default_txt)
            self.err.setText(self.c_flow)
            self.answer = str(res)
            self.lbl_answer.setText(self.answer)

    def clear(self) -> None:
        self.lbl_answer.setText('Answer')
        self.err.setText(self.err_txt)
        self.input_line.setText('')

    def quit(self) -> None:
        self.window.destroy()
        QApplication.quit()


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    calculator: Calculator = Calculator()
    calculator.window.show()
    sys.exit(app.exec_())
        
