import sys
import termios
import tty
from typing import Callable

def main():
    hinput("prompt: ", on_char)
    return 0

def on_char(ch: str, line: str) -> bool:
    if ch == 'x':
        sys.stdout.write('\n')
        sys.stdout.flush()
        return True
    if line+ch == 'hello':
        sys.stdout.write("%s, world\n" % ch)
        sys.stdout.flush()
        return True
    return False

def hinput(prompt: str=None, hook: Callable[[str,str], bool]=None) -> str:
    """input with a hook for char-by-char processing."""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    inpt = ""
    while True:
        sys.stdout.write('\r')
        if prompt is not None:
            sys.stdout.write(prompt)
        sys.stdout.write(inpt)
        sys.stdout.flush()
            
        ch = None
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

        if hook is not None and hook(ch, inpt):
            break

        if ord(ch) == 0x7f: #BACKSPACE
            if len(inpt) > 0:
                sys.stdout.write('\b \b')
                inpt = inpt[:-1]
            continue

        if ord(ch) == 0x0d: #ENTER
            sys.stdout.write('\n')
            sys.stdout.flush()
            break

        if ch.isprintable():
            inpt += ch
            
    return inpt

if __name__ == '__main__':
    sys.exit(main())