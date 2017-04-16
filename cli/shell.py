import readline
import sys
from cli.shell_completer import ShellCompleter

commands = [
    'help',
    'exit'
    ]


def help():
    print("help")


def exit():
    print("bye")
    sys.exit(0)


completer = ShellCompleter(list(set(commands)))
readline.set_completer_delims(' \t\n;')
readline.set_completer(completer.complete)
readline.parse_and_bind("bind ^I rl_complete")
readline.set_completion_display_matches_hook(completer.display_matches)
print('diag shell\n\t')
while True:
    command = input("diag> ")
    if command in locals():
        locals()[command]()
    else:
        print("command not found")
