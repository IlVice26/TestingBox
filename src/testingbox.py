"""
TestingBox main file
"""

import subprocess
import argparse
import curses

__author__ = 'Elia Vicentini'
__version__ = '0.1'

# Global variables
verbose = False


def ctrl_lib():
    """Check if the required libraries are installed in the system"""

    try:  # Check if pip3 is installed on the system
        subprocess.check_output('pip3')
    except FileNotFoundError:
        print("Pip3 is not installed on your system. \n"
              "Download it via https://bootstrap.pypa.io/get-pip.py "
              "and start it with 'python3 get-pip.py'.")

    cmd_libraries = subprocess.Popen(['pip3', 'list'], stdout=subprocess.PIPE)  # Obtaining the installed libraries
    i_libraries = str(cmd_libraries.stdout.read())  # Reading the output of the command 'pip3 list'
    cmd_libraries.stdout.close()

    try:
        with open('../requirements.txt', 'r') as requirements:
            lines = requirements.readlines()  # Reading every line in 'requirements.txt' and save them in 'lines' array

            not_installed = []
            for i in lines:  # Checking if a required library is installed
                if i not in i_libraries:
                    temp = i.replace('\n', '')
                    not_installed.append(temp)

            if len(not_installed) > 1:
                temp = ""
                for i in range(len(not_installed)):
                    temp += "'" + not_installed[i] + "' "
                print("These libraries " + temp + "are not installed. Please install them via pip3")
                exit(1)
            elif len(not_installed) == 1:
                print("The library '{0}' is not installed. Please install it via pip3".format(not_installed[0]))
                exit(1)
            else:
                if verbose:
                    print("Libraries are OK")
                return True
    except FileNotFoundError:
        print("The file 'requirements.txt' has not been found. Check if it is present in the directory or clone the "
              "repository again from Github")


def menu():
    """View the menu and its choices"""

    win = curses.initscr()
    win.erase()

    win.addstr(0, 0, "-------------------------------------------------------\n"
                     "|                  TestingBox v. " + __version__ + '                  |\n'
                     '-------------------------------------------------------\n\n'
                     'H) Test Hard Disk\n'
                     '\n'
                     'I) View program information\n'
                     'Q) Quit\n'
                     '\n'
                     'Enter your choice: ')

    choice = win.getstr().decode('utf-8').lower()
    win.refresh()

    if choice == 'h':
        pass
    elif choice == 'i':
        pass
    elif choice == 'q':
        exit(0)
    else:
        win.erase()
        menu()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='TestingBox')
    parser.add_argument('-v', help='verbose', action='store_true')
    args = vars(parser.parse_args(args=None))

    if args['v'] is True:
        verbose = True

    if ctrl_lib():
        menu()
