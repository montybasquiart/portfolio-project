#!/usr/bin/python3
# A simple shell command interpreter
import cmd

class Shell(cmd.Cmd):
    """A simple command processor.
    """
    def do_greet(self, line):
        print("Hello", line)

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    Shell().cmdloop()
