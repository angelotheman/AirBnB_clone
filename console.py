#!/usr/bin/python3
"""
Command Line interpreter program
- class: HBNBCommand
- This should implement
    - quit and EOF
    - help
    - prompt (hbnb)
    - empty line shouldn't execute anything
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of the interpreter.
    Defines the commands used to interract with the program
    """

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
        """

        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            class_map = {
                    'BaseModel': BaseModel,
                }
            if class_name in class_map:
                class_instance = class_map[class_name]()
                storage.new(class_instance)
                storage.save()
                print(class_instance.id)
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
