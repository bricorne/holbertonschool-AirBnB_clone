#!/usr/bin/python3
"""create a console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """create a prompt"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        return True

    def do_quit(self, arg):
        """Quit commant to exit the program"""
        return True

    def emptyline(self):
        """Do anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
