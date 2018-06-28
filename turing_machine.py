#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tape import Tape

class TuringMachine(object):
    """
    TuringMachine(machine_config, tape_content)

        machine_config is a list of attributes of the Turing machine that must be like following:
            position 0: List of the input alphabet
            position 1: List of the tape alphabet
            position 2: Symbol that represents the blank space
            position 3: List of the states
            position 4: The initial state
            position 5: List of the final states
            position 6: Number of tapes (This Turing machine simulator currently accepts only single-tape machines)
            position 7 to forward: Transactions in a list format that must be like:
                position 0: Currently state
                position 1: Next state
                position 2: The symbol of tape in current position
                position 3: The New symbol of tape in current position
                position 4: The indication of movement (R to right, L to left and S to stay)

        tape_content is a String that represents the content on the tape at begin of Turing machine computing
    """
    def __init__(self, machine_config, tape_content):
        self.input_alphabet = machine_config[0]
        self.tape_alphabet = machine_config[1]
        self.blank_symbol = ''.join(machine_config[2])
        self.states = machine_config[3]
        self.init_state = ''.join(machine_config[4])
        self.final_states = machine_config[5]
        self.qnt_tapes = int(''.join(machine_config[6]))
        self.transictions = machine_config[7:]
        self.tape_content = tape_content
        self.tape = Tape(self.tape_content, self.blank_symbol)

    def initialize_computing(self):
        """
        initialize_computing()

        Initializes the Turing machine computing
        """
        self.print_information()
        current_state = self.init_state
        queue = [self.tape]
        while queue:
            if current_state in self.final_states:
                print(self.tape.tape_content)
                print('Accept')
                exit(0)

            valid_transitions = self.valid_transitions(current_state)

            for transition in valid_transitions:
                current_state = self.aply_transaction(transition)


    def validate_input(self):
        """
        validate_input()

        Input format validation

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
        if self.input_alphabet == ['']:
            return 1
        if self.tape_alphabet == ['']:
            return 2
        if self.blank_symbol == '':
            return 3
        if self.states == ['']:
            return 4
        if self.init_state == '':
            return 5
        if self.final_states == ['']:
            return 6
        if self.qnt_tapes != 1:
            return 7
        if self.transictions == []:
            return 8
        for character in list(self.tape_content)
        if self.transictions == []:
            return
        return 0

    def print_information(self):
        print('Input alphabet: ', self.input_alphabet)
        print('Tape alphabet: ', self.tape_alphabet)
        print('Blank symbol: ', self.blank_symbol)
        print('States: ', self.states)
        print('Initial state: ', self.init_state)
        print('Final states: ', self.final_states)
        print('Quantity of tapes', self.qnt_tapes)

    def aply_transaction(self, transition):
        self.tape.write(transition[3])
        self.tape.move(transition[4])
        return transition[1]

    def valid_transitions(self, state):
        valid_transitions = []
        for transiction in self.transictions:
            if transiction[0] == state:
                if self.tape.read() == transiction[2]:
                    valid_transitions.append(transiction)
        return valid_transitions
