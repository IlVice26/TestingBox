"""
TestingBox main file
"""

import subprocess

__author__ = 'Elia Vicentini'
__version__ = '0.1'


def ctrl_lib():
    """Check if the required libraries are installed in the system"""

    try:  # Check if pip3 is installed on the system
        subprocess.check_output('pip3')
    except FileNotFoundError:
        print("Pip3 is not installed on your system. \n"
              "Download it via https://bootstrap.pypa.io/get-pip.py "
              "and start it with 'python3 get-pip.py'.")

    cmd_libraries = subprocess.Popen(['pip3 list'], stdout=subprocess.PIPE)  # Obtaining the list of installed libraries
    i_libraries = str(cmd_libraries.stdout.read())  # Reading the output of the command 'pip3 list'

    with open('../requirements.txt', 'r') as requirements:
        lines = requirements.readlines()  # Reading every line in 'requirements.txt' and save them in 'lines' array

        for i in lines:  # Checking if a required library is installed
            if i not in i_libraries:
                print(
                    'Library {0} not installed. \nPlease install this library using \'pip3 install {1}\''.format(i, i))


if __name__ == '__main__':
    ctrl_lib()
