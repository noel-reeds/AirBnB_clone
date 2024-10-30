#!/usr/bin/python3
"""The console module"""
import cmd
from models.base_model import BaseModel as base
from models import storage as store
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, *args):
        """Exits the console."""
        print("Thank you and goodbye!")
        return True

    def do_EOF(self, *args):
        """Exits the program"""
        print("Goodbye!")
        return True

    def do_create(self, args):
        """Creates an instance of BaseModel."""
        cmd_cls = args.split()
        if len(cmd_cls) != 1:
            print("** class name missing **")
            return
        elif cmd_cls[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        try:
            bm = base()
            store.save()
            print(bm.id)
        except Exception as err:
            print(err)

    def do_show(self, args):
        """Prints str rep of an obj based on class name and id"""
        cls_id = args.split()
        if len(cls_id) == 0:
            print("** class name missing **")
            return
        elif len(cls_id) != 2:
            print("** instance id missing **")
            return
        elif cls_id[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        try:
            store.reload()
            all_objs = store.all()
            key = f"{cls_id[0]}.{cls_id[1]}"
            if key in all_objs.keys():
                print(all_objs[key])
            else:
                print("** no instance found **")
        except Exception as err:
            print(err)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        cls_id = args.split()
        if len(cls_id) == 0:
            print("** class name missing")
            return
        elif len(cls_id) != 2:
            print("** instance id missing **") 
            return
        elif cls_id[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        try:
            store.reload()
            all_objs = store.all()
            type(all_objs)
            key = f"{cls_id[0]}.{cls_id[1]}"
            if key in all_objs.keys():
                all_objs.pop(key)
                store.save()
                return
            else:
                print("** no instance found **")
        except (Exception, FileNotFoundError) as err:
            print(err)

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
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
