#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tape(object):

    def __init__(self, tape_content, blank_symbol):
        self.reading_head = 0
        self.tape_content = list(tape_content)
        self.blank_symbol = blank_symbol

    def move(self, direction):
        """
        Move reading head one unit on the tape in a given direction
        (R to right, L to left or S to stay).
        If the reading head passes one of the extremities of the tape one
        blank symbol is added. This way the tape keep being infinite.
        """
        if direction == 'R':
            self.reading_head += 1
            if self.reading_head == len(self.tape_content):
                self.tape_content.append(self.blank_symbol)

        if direction == 'L':
            self.reading_head -= 1
            if self.reading_head < 0:
                self.reading_head = 0
                self.tape_content.insert(0, self.blank_symbol)

        if direction == 'S':
            pass

    def read(self):
        """
        Returns the symbol of the tape where the reading head is.
        """
        return self.tape_content[self.reading_head]

    def write(self, symbol):
        """
        Overwrites the symbol of the tape where the reading head is with a
        given symbol.
        """
        self.tape_content[self.reading_head] = symbol
