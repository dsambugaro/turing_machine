#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

from turing_machine import Turingmachine

class Maincontroller(object):
    def __init__(self, file):
        self._file_content = self._parse_file_(file)
        self._turing_machine = Turingmachine(self._file_content)

    def _parse_file_(self, file):
        file_content = []
        with open(file, 'r') as f:
            for line in f:
                aux = line.rstrip().split(' ')
                file_content.append(aux)
        return file_content

    def init_turing(self):
        self._turing_machine.process()

    def validade_turing(self):
        self._turing_machine.validade()

def main():
        file = argv[1]
        print('Parsing file')
        mc = Maincontroller(file)
        print('Validating')
        mc.validade_turing()
        mc.init_turing()

if __name__ == '__main__':
    main()
