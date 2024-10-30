#!/usr/bin/python3
"""The console module"""
import cmd
from models.base_model import BaseModel as base
from models import storage as store
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    models = [
        "BaseModel", "User", "Place",
        "State", "City", "Amenity","Review"
        ]

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
        elif cmd_cls[0] not in self.models:
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
        elif cls_id[0] not in self.models:
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
            print("** class name missing **")
            return
        elif len(cls_id) != 2:
            print("** instance id missing **") 
            return
        elif cls_id[0] not in self.models:
            print("** class doesn't exist **")
            return
        try:
            store.reload()
            all_objs = store.all()
            key = f"{cls_id[0]}.{cls_id[1]}"
            if key in all_objs.keys():
                all_objs.pop(key)
                store.save()
                return
            else:
                print("** no instance found **")
        except (Exception, FileNotFoundError) as err:
            print(err)

    def do_all(self, args):
        """Prints str rep of all instances based or not on cls name"""
        cls_name = args.split()
        if len(cls_name) == 0:
            store.reload()
            all_objs = store.all()
            [print(obje) for obje in all_objs.values()]
            return
        elif len(cls_name) == 1 and cls_name[0] not in self.models:
            print("** class doesn't exist **")
            return
        elif cls_name[0] in self.models:
            store.reload()
            all_objs = store.all()
            [print(obje) for obje in all_objs.values()]
            return

    def emptyline(self):
        """Overwrites default empty line."""
        pass

    def do_update(self, args):
        """Updates an instance based on the cls name and id."""
        cls_attr = args.split()
        if len(cls_attr) == 0:
            print("** class name missing **")
            return
        elif cls_attr[0] not in self.models:
            print("** class doesn't exist **")
            return
        elif len(cls_attr) == 1:
            print("** instance id missing **")
            return
        key = f"{cls_attr[0]}.{cls_attr[1]}"
        store.reload()
        all_objs = store.all()
        if key not in all_objs.keys():
            print("** no instance found **")
            return
        elif len(cls_attr) == 2:
            print("** attribute name missing **")
            return
        elif len(cls_attr) == 3:
            print("** value missing **")
            return
        new_attr = cls_attr[2]
        new_value = cls_attr[3].strip('"')
        assert key in all_objs.keys()
        modified = all_objs[key]
        modified.__dict__[new_attr] = new_value
        store.save()
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
