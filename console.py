#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    intro = "Hello, type 'help' and start exploring.."
    prompt = "(hbnb)"

    def do_quit(self, *args):
        """Exits the console."""
        print("Thank you and goodbye!")
        return True

    def do_EOF(self, *args):
        """Exits the program"""
        print("Goodbye!")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
