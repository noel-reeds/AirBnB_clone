#!/usr/bin/python3
"""The console module"""
import cmd
from models.base_model import BaseModel
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, *args):
        """
        Exits the console.
        """
        print("Thank you and goodbye!")
        return True

    def do_EOF(self, *args):
        """
        Exits the program
        """
        print("Goodbye!")
        return True

    def do_create(self, *args):
        """
        Creates an instance of BaseModel.
        """
        if args == 1:
            print("** class name missing **")
        elif sys.argv[1] is not BaseModel:
            print("** class doesn't exist **")
        obj = BaseModel()
        FileStorage.save(obj)
        print(obj.id)

    def do_show(self, *args):
        """
        Prints a str rep of an instance based
        on class name and id.
        """
        if args == 1:
            print("** class name missing **")
        elif sys.argv[1] is not BaseModel:
            print("** class doesn't exist **")
        elif args == 2:
            print("** instance id missing **")
        elif sys.argv[2] not in object_dict.keys():
            print("** no instance found **")
        return object_dict[sys.argv[2]]

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        """
        if args == 1:
            print("** class name missing")
        elif sys.argv[1] is not BaseModel:
            print("** class doesn't exist **")
        if args == 2:
            print("** instance id missing **")
        elif sys.argv[2] not in object_dict.keys():
            print("** no instance found **")
        del object_dict[sys.argv[2]]
        BaseModel.save(self)

    def do_all(self, *args):
        """
        Prints str representation of all
        instances based or not on the class name
        """
        if args == 2 and sys.argv[1] is not BaseModel:
            print("** class doesn't exist **")
        elif args == 1 and sys.argv[0] == "all":
            print("** class doesn't exist **")
        else:
            final_dict = BaseModel.to_dict(self)
            return final_dict

    def emptyline(self):
        """
        Overwrites default empty line.
        """
        pass

    def do_update(self, *args):
        """
        Updates an instance based on the class name and id.
        """
        pass


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sysargv[1:]))
    else:
        HBNBCommand().cmdloop("Karibu, type 'help' and start exploring.")
