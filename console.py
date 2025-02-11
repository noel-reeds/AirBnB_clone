#!/usr/bin/python3
"""The console module"""
import ast
import cmd
from models.base_model import BaseModel as base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage as store


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "User": User, "Amenity": Amenity, "City": City,
        "Place": Place, "State": State, "Review": Review, "BaseModel": base
        }

    def do_quit(self, args):
        """Exits the console."""
        return True

    def do_EOF(self, args):
        """Exits the program"""
        return True

    def do_create(self, args):
        """Creates an instance of BaseModel."""
        cmd_cls = args.split()
        if len(cmd_cls) != 1 or len(cmd_cls) > 1:
            print("** class name missing **")
            return
        elif cmd_cls[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        try:
            cls_key = cmd_cls[0]
            cls = self.classes.get(cls_key)
            obje = cls()
            store.save()
            print(obje.id)
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
        elif cls_id[0] not in self.classes.keys():
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
        elif cls_id[0] not in self.classes.keys():
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
        elif len(cls_name) == 1 and cls_name[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        elif cls_name[0] in self.classes.keys():
            store.reload()
            all_objs = store.all()
            [print(obje) for obje in all_objs.values()]
            return
        cls_name = args.split(".")
        assert len(cls_name) == 2
        assert cls_name[1] == "all()"
        assert cls_name[0] in self.classes.keys()
        store.reload()
        all_objs = store.all()
        objs = []
        for key in all_objs.keys():
            cls_id = key.split(".")
            assert cls_id[0] == cls_name[0]
            objs.append(all_objs[key])
        [print(obje) for obje in objs]

    def emptyline(self):
        """Overwrites default empty line."""
        pass

    def do_update(self, args):
        """Updates an instance based on the cls name and id."""
        cls_attr = args.split()
        if len(cls_attr) == 0:
            print("** class name missing **")
            return
        elif cls_attr[0] not in self.classes.keys():
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

    def default(self, args):
        """Overwrite the default method"""
        methods = ["all()", "count", "show", "update"]
        cls_fn = args.split(".")
        if len(cls_fn) == 2 and cls_fn[0] in self.classes.keys():
            if cls_fn[1] == "all()":
                store.reload()
                all_objs = store.all()
                tar_objs = []
                for key in all_objs.keys():
                    cls_id = key.split(".")
                    if cls_fn[0] in cls_id:
                        tar_objs.append(all_objs[key])
                [print(obj) for obj in tar_objs]
            elif cls_fn[1] == "count()":
                store.reload()
                all_objs = store.all()
                count = 0
                for key in all_objs.keys():
                    cls_id = key.split(".")
                    if cls_fn[0] in cls_id:
                        count += 1
                print(count)
            elif "show" in cls_fn[1]:
                obje_id = cls_fn[1].strip('show(")')
                if obje_id == "":
                    print("** instance id missing **")
                    return
                store.reload()
                objs = store.all()
                key = f"{cls_fn[0]}.{obje_id}"
                if key in objs.keys():
                    print(objs[key])
                    return
                print("** no instance found **")
            elif "destroy" in cls_fn[1]:
                obje_id = cls_fn[1].strip('destroy(")')
                if obje_id == "":
                    print("** instance id missing **")
                    return
                store.reload()
                objs = store.all()
                key = f"{cls_fn[0]}.{obje_id}"
                if key in objs.keys():
                    objs.pop(key)
                    store.save()
                    return
                print("** no instance found **")
            elif "update" in cls_fn[1]:
                args = cls_fn[1].strip("update()")
                if args == "":
                    print("** instance id missing **")
                    return
                tup = ast.literal_eval(args)
                if type(tup) is str:
                    print("** attribute name missing **")
                    return
                store.reload()
                objs = store.all()
                obj_id = tup[0]
                key = f"{cls_fn[0]}.{obj_id}"
                if key not in objs.keys():
                    print("** no instance found **")
                    return
                elif len(tup) == 1:
                    print("** attribute name missing **")
                    return
                elif len(tup) == 2:
                    if type(tup[1]) is dict:
                        for key_id, value_id in tup[1].items():
                            objs[key].__dict__[key_id] = value_id
                        store.save()
                        return
                    print("** value missing **")
                    return
                objs[key].__dict__[tup[1]] = tup[2]
                store.save()
            else:
                self.stdout.write("*** Uknown syntax: %s\n" % args)
        else:
            self.stdout.write("*** Uknown syntax: %s\n" % args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
