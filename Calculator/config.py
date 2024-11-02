# Window cofig

SIZE: int = 32
ROWS: int = 30
COLS: int = 35
WND_WIDTH: int = SIZE * COLS
WND_HEIGHT: int = SIZE * ROWS
WND_SIZE: tuple[int, int] = WND_WIDTH, WND_HEIGHT
SHIFT_X: int = SIZE * 3
SHIFT_Y: int = SIZE * 5
WND_SHIFT: tuple[int, int] = SHIFT_X, SHIFT_Y
TITLE: str = 'Simple calculator'

# Paths
FILE_HELP: str = 'Assets/Help.txt'
FONT_PATH: str = 'Assets/SUSE-Bold.ttf'
ICON_PATH: str = 'Assets/Calculator.png'

# Consts
FNT_SIZE: int = int(SIZE * .5) 
