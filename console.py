#!/usr/bin/python3
"""create a console"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """create a prompt"""
    prompt = '(hbnb) '
    list_class = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                  'Place', 'Review']

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        return True

    def do_quit(self, arg):
        """Quit commant to exit the program"""
        return True

    def emptyline(self):
        """Do anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.strip()
        try:
            model_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        new_instance = model_class()
        new_instance.save()
        print(new_instance.id)
    
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        inst_id = args[1]

        key = "{}.{}".format(class_name, inst_id)
        instances = FileStorage().all()

        if key in instances:
            instance = instances[key]
            print(instance)
        else:
            print('** no instance found **')
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]

        if class_name not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        inst_id = args[1]  

        try:
            obj_to_del = FileStorage().all()
            string = "{}.{}".format(class_name, inst_id)
            del obj_to_del[string]
            FileStorage().save()
        except:
            print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg = arg.split()
        objects = FileStorage().all()

        if len(arg) == 0:
            print([str(obj) for obj in objects.values()])
        elif arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == arg[0]])
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]

        if class_name not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        inst_id = args[1]  
        
        key = "{}.{}".format(class_name, inst_id)
        instances = FileStorage().all()

        if key in instances:
            instance = instances[key]
        else:
            print('** no instance found **')
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return
        setattr(instance, args[2], args[3])
        FileStorage().save()

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
