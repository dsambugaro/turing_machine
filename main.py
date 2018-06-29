#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

from turing_machine import TuringMachine

class Maincontroller(object):
    """
    Maincontroller()

    This class parses the input file, then create an
    instance of a Turing machine.
    Also is responsible to access a validate method of
    Turing machine and initialize your computing
    """
    def __init__(self, file, tape_content):
        self._file_content = self._parse_file_(file)
        self._tape_content = tape_content
        self._turing_machine = TuringMachine(self._file_content, self._tape_content)

    def _parse_file_(self, file):
        file_content = []
        try:
            with open(file, 'r') as f:
                for line in f:
                    # Remove all leading and trailing characters (\n \r \t) of the line
                    # Transforms the line into a list, spliting in ' '
                    # Then append the list in "file_content"
                    file_content.append(line.strip().split(' '))
            return file_content
        except IOError:
            print('Error opening file for reading.')
            print('The file exists and you have read permissions?')
            exit(1)

    def validate(self):
        """
        validate()

        Input format validation.

        returns 0 if the input format is valid or one of the following for invalid:
            1 if has no one input alphabet detected
            2 if has no one tape alphabet detected
            3 if has no one blank symbol detected
            4 if has no one states detected
            5 if has no one init state detected
            6 if has no one final state detected
            7 if the quantity of tapes is different of 1
            8 if has no one transition detected
        """
        return self._turing_machine.validate_input()

    def init_turing(self):
        """
        Initialize the computing of Turing machine
        """
        self._turing_machine.initialize_computing()

def main():
    """
    Main method

    Validate command line parameters and create a instance of
    Maincontroller class.
    Then he validates machine attributes parsed from file and if it's ok the
    Turing machine computation initializes.
    """
    if len(argv) != 3:
        print('\n')
        print('Usage:')
        print('\t$ python {} <turing machine file> <content of tape>'.format(argv[0]))
        print('Exemple:')
        print('\t$ python main.py copy_turing_machine.txt 111')
        print('\n')
        exit(1)

    file = argv[1]
    tape_content = argv[2]
    print('\nLOG:\n')
    print('Parsing file')
    mc = Maincontroller(file, tape_content)
    print('File parsed')
    print('Validating input file')
    try:
        validate = mc.validate()
        if validate != 0:
            raise Exception("Input file invalid!")
    except Exception as e:
        print(e)
        exit(1)
    print('Input file validated')
    print('Initializing Turing machine...')
    print('\n\n')
    mc.init_turing()

if __name__ == '__main__':
    main()
