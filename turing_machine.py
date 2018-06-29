#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tape import Tape
from copy import copy

class TuringMachine(object):
    """
    Executes Turing machine's computing, in a way that applies transitions and
    puts every possible configuration from the current state in a queue.
    Resolves transitions of each configuration of the queue, removing invalid
    configurations and adding new configurations to the queue if necessary.
    This process continues until the computing accepts or reject the entry.
    This class also has a method, called validate_input, that when used checks
    if the machine attributes are correct.

    TuringMachine(machine_config, tape_content)

        machine_config is a list of attributes of the Turing machine that must be like following:
            position 0: List of the input alphabet
            position 1: List of the tape alphabet
            position 2: Symbol that represents the blank space
            position 3: List of the states
            position 4: The initial state
            position 5: List of the final states
            position 6: Number of tapes (This Turing machine simulator currently accepts only single-tape machines)
            position 7 to forward: transitions in a list format that must be like:
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
        queue = [[self.tape, self.init_state]]
        print('Computing...')
        while queue:
            current = queue.pop()
            if current[1] in self.final_states:
                print('Tape content: ', ' '.join(current[0].tape_content))
                print('Accepted')
                exit(0)

            valid_transitions = self.valid_transitions(current[1], current[0])

            for transition in valid_transitions:
                aux = self.aply_transition(transition, current[0])
                queue.append(aux)

        print('Tape content: ', ' '.join(current[0].tape_content))
        print('Rejected')
        exit(0)


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
        return 0

    def print_information(self):
        print('======= About this Turing machine =======')
        print('Input alphabet: ', self.input_alphabet)
        print('Tape alphabet: ', self.tape_alphabet)
        print('Blank symbol: ', self.blank_symbol)
        print('States: ', self.states)
        print('Initial state: ', self.init_state)
        print('Final states: ', self.final_states)
        print('Quantity of tapes', self.qnt_tapes)
        print('=========================================')
        print('\n\n')

    def aply_transition(self, transition, tape):
        new_tape = copy(tape)
        new_tape.write(transition[3])
        new_tape.move(transition[4])
        return [new_tape, transition[1]]

    def valid_transitions(self, state, tape):
        valid_transitions = []
        for transiction in self.transictions:
            if transiction[0] == state:
                if tape.read() == transiction[2]:
                    valid_transitions.append(transiction)
        return valid_transitions
