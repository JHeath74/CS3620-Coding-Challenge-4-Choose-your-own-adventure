class Colors:
    """ ANSI color codes """
    # ---------Normal Colors---------------------------

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    YELLOW = "\033[1;33m"

    # ---------Light Colors---------------------------

    LIGHT_GRAY = "\033[0;37m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"

    # ---------Dark Colors---------------------------

    DARK_GRAY = "\033[1;30m"

    # ---------BackGround Colors---------------------------

    BackgroundBlack = "\u001b[40m"
    BackgroundRed = "\u001b[41m"
    BackgroundGreen = "\u001b[42m"
    BackgroundYellow = "\u001b[43m"
    BackgroundBlue = "\u001b[44m"
    BackgroundMagenta = "\u001b[45m"
    BackgroundCyan = "\u001b[46m"
    BackgroundWhite = "\u001b[47m"
    BackgroundBrightBlack = "\u001b[40;1m"
    BackgroundBrightRed = "\u001b[41;1m"
    BackgroundBrightGreen = "\u001b[42;1m"
    BackgroundBrightYellow = "\u001b[43;1m"
    BackgroundBrightBlue = "\u001b[44;1m"
    BackgroundBrightMagenta = "\u001b[45;1m"
    BackgroundBrightCyan = "\u001b[46;1m"
    BackgroundBrightWhite = "\u001b[47;1m"

    # ---------- Fonts---------------------------------

    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"

    # --------Reset Colors back to original color-----
    Reset = "\033[39m"

    END = "\033[0m"
