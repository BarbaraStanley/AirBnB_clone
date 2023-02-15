#!/usr/bin/python3
""" Entry point for the command line interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Defines the command line interpreter class
    """

    prompt = '(hbnb) '
    # dict_classes = {'BaseModel': BaseModel}

    def emptyline(self):
        """Do nothing when only a newline character is passed """
        pass

    def do_quit(self, args):
        """ Exit the program """
        return True

    def do_EOF(self, args):
        """ End of file character and quits the program """
        print()
        return True

    def do_create(self, cls):
        """ Create a new instance of BaseModel saves it to the JSON
        file and prints its id
        Args:
            cls : The class Name of the instance
        Usage:
            <create BaseModel>
        """

        if cls == "":
            print("** class name missing **")
        if cls != "BaseModel":
            print("** class doesn't exist **")
        else:
            # classes = {'BaseModel': BaseModel}
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based on
        the class name and id.
        Args:
            args: The classname and id
        Usage:
            <show BaseModel 1234-1234-abde>
        """

        if args is None:
            print("** class name missing **")
        l_arg = args.split(' ')
        if l_arg[0] != BaseModel:
            print("** class doesn't exist ** ")
        if l_args[1] == "":
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(l_arg[0], l_arg[1])
            if key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[key])

    def do_destroy(self, args):
        """ Deletes the instance based on the class name and id
        saves the changes to the JSON file
        Args:
            args: The class nname and id
        Usage:
            <destroy BaseModel 1234-1234-abde>
        """

        if args is None or args == "":
            print("** class name missing **")
        l_arg = args.split(' ')
        if l_args[0] is not BaseModel:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storaage.all()
            key = "{}.{}".format(l_arg[0], l_arg[1])
            if key not in all_objs:
                print("** no instance found **")
            else:
                del (all_objs[key])

    def do_all(self, args):
        """ Prints all the string representaion of all instances based
        or nor based on the class name
        Args:
            args: Classname
        Usage:
            <all BaseModel> or <all>
        """

        if args != "":
            l_arg = args.split(' ')
            if l_arg[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                l_str_obj = []
                all_objs = storage.all()
                for key, value in all_objs.items():
                    obj_name = value.__class.__name__
                    if l_arg[0] == obj_name:
                        l_str_obj = l_str_obj.append(eval("obj_name"))
                print(l_str_obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
