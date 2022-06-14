import colorama as c


# COLORAMA KEYS
fore_dict = {
        'r': c.Fore.RED,
        'g': c.Fore.GREEN,
        'b': c.Fore.BLUE,
        'c': c.Fore.CYAN,
        'm': c.Fore.MAGENTA,
        'y': c.Fore.YELLOW,
        'w': c.Fore.WHITE
    }

back_dict = {
    'r': c.Back.RED,
    'g': c.Back.GREEN,
    'b': c.Back.BLUE,
    'c': c.Back.CYAN,
    'm': c.Back.MAGENTA,
    'y': c.Back.YELLOW,
    'w': c.Back.WHITE
}

style_dict = {
    'd': c.Style.DIM,
    'n': c.Style.NORMAL,
    'b': c.Style.BRIGHT
}
# /COLORAMA KEYS

def colorama_init():
    c.init()


def txt_color(txt: str, fg='x', bg='x'):
    color_str = ''

    if fg != 'x':
        fg_color, fg_style = fg[0], fg[1]
    else:
        fg_color, fg_style = 'w', 'n'
    color_str += fore_dict[fg_color] + style_dict[fg_style]

    if bg != 'x':
        bg_color, bg_style = bg[0], bg[1]
        color_str += back_dict[bg_color] + style_dict[bg_style]
        
    formatted = color_str + txt + c.Style.RESET_ALL
    return formatted

