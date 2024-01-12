#!/usr/bin/python3
"""
Command Line interpreter program
- class: HBNBCommand
- This should implement
    - quit and EOF
    - help
    - prompt (hbnb)
    - empty line shouldn't execute anything
- Implement the following commands
    - create
    - show
    - destroy
    - all
    - update
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of the interpreter.
    Defines the commands used to interract with the program
    """

    prompt = "(hbnb) "

    class_map = {
            'BaseModel': BaseModel,
        }

    def do_EOF(self, line):
        """
        Ends the program with Ctrl + D
        """
        return True

    def do_quit(self, line):
        """
        Ends the program if quit is entered
        """
        return True

    def emptyline(self):
        """
        Called when an emptyline is encountered
        """
        pass

    def do_create(self, line):
        """
        - Creates a new instance of BaseModel
        - Saves it to the JSON file
        - Prints the id
        - Usage: ($) create <model_name>
        """

        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in self.class_map:
                class_instance = self.class_map[class_name]()
                storage.new(class_instance)
                storage.save()
                print(class_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        - Prints the string representation of an instance
        - If class name is missing print ** class name missing **
        - if class name doesn't exist print ** class doesn't exist **
        - If id is missing print ** instance id is missing
        - If instance of classname doesn't exist print **no instance found**
        - Usage: ($) show <class_name> id
        """
        args = line.split()

        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.class_map:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                all_objects = storage.all()

                if key not in all_objects:
                    print("** no instance found **")
                else:
                    print(all_objects[key])

    def do_destroy(self, line):
        """
        - Deletes an instance based on the classname and id
        - If class name is missing print ** class name missing **
        - If classname doesn't exist print ** classname doesn't exist**
        - If id is missing print **instance id missing**
        - If instance of class name doesn't exist for given id print
            ** no instance found **
        - Usage: ($) destroy <class_name> id
        """
        args = line.split()

        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.class_map:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                all_objects = storage.all()

                if key not in all_objects:
                    print("** no instance found **")
                else:
                    del all_objects[key]

    def do_all(self, line):
        """
        - Prints all string representation of all instances
        - This is based or not based on the class name
        - If class name doesn't exist print ** class doesn't exist **
        - Usage:
            1. ($) all BaseModel
            2. ($) all
        """
        args = line.split()

        all_objects = storage.all()

        print(
            [str(obj) for obj in all_objects.values()]
            if not args or args[0] in self.class_map
            else "** class doesn't exist **"
        )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
