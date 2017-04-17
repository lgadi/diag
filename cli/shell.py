import inspect
import logging
import readline
import sys

import cli.handlers
from cli.shell_completer import ShellCompleter

logger = logging.getLogger(__name__)

commands = []


class Shell:
    def __init__(self):
        self.fill_commands("")
        completer = ShellCompleter(list(set(commands)))
        readline.set_completer_delims(' \t\n;')
        readline.set_completer(completer.complete)
        readline.parse_and_bind("bind ^I rl_complete")
        readline.set_completion_display_matches_hook(completer.display_matches)

        print('diag shell\n\t')

    def help(self):
        print("help")

    def exit(self):
        print("bye")
        sys.exit(0)

    def get_classes_in_module(self, _module, classes):
        ch = getattr(cli.handlers, _module)
        for name, obj in inspect.getmembers(ch):
            if inspect.isclass(obj):
                classes.append(obj)

    def fill_commands(self, context):
        if context is "":
            commands.append('help')
            commands.append('exit')
            handler_modules = cli.handlers.get_classes()
            classes = []
            for hm in handler_modules:
                self.get_classes_in_module(hm, classes)
            for cls in classes:
                c = cls()
                if c.handler_name() is not None:
                    commands.append(c.handler_name())

    def run(self):
        while True:
            command = input("diag> ")
            method = getattr(self, command)
            if method:
                method()
            else:
                print("command not found")


if __name__ == "__main__":
    shell = Shell()
    shell.run()
