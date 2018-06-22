#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Turingmachine(object):
    def __init__(self, file_content):
        self.input_alphabet = file_content[0]
        self.tape_alphabet = file_content[1]
        self.blank_symbol = ''.join(file_content[2])
        self.states = file_content[3]
        self.init_state = ''.join(file_content[4])
        self.final_states = file_content[5]
        self.qnt_tapes = int(''.join(file_content[6]))
        self.transictions = file_content[7:]

    def process(self):
        print('uhul')
