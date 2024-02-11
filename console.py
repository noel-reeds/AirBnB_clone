#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    intro = "Karibu, type 'help' and start exploring.."
    prompt = "(hbnb)"

    def do_quit(self, *args):
        """Exits the console."""
        print("Thank you and goodbye!")
        return True

    def do_EOF(self, *args):
        """Exits the program"""
        print("Goodbye!")
        return True

    def do_create(self, *args):
        """Creates an instance of BaseModel"""
        obj = BaseModel()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
