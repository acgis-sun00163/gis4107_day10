# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import os


def main():
    pass

def get_file_content(file_name):
    with open(file_name) as in_file:
        content =in_file.read()
    return content





def get_exist_file(file_name):
    try:
        with open(file_name) as in_file:
            content =in_file.read
        return content
    except IOError:
        return "{} does not exist.".format(file_name)


def write_to_file (file_name, content):
    file_route = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data",file_name)

    with open(file_name,"a") as writer:
        writer.write(content)
    return (get_file_content(file_name))






def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass

if __name__ == '__main__':
    main()