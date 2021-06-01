#!/usr/bin/env python3


import subprocess
import os 
import re 
import time 
from iodata import load_one, dump_one , formats
from ase.io import xyz
from ase.io import read, write
from shutil import copyfile
from sys import exit


def shell_copy_template(srcdir, filename):
    """
    check into srcdir,
    then copy the file called filename_template.sh to filename.sh
    return filename.sh as a python string
    """
    the_template =f'{srcdir}/{filename}_template.sh'
    the_file =f'{srcdir}/{filename}.sh'
    copyfile(the_template,the_file)
    return the_file

# Python templates for development purpose
class MyClass:
    def __init__(self,parm1, parm2):
        self.parm1 = parm1
        self.parm2 = parm2
    
    def myfunction(self):
        print("test,test, this is " + self.parm1 )

#Test Deploy zone
p1 = MyClass("parm1", 33)

print(p1.parm1)
print(p1.parm2)

p1.myfunction()