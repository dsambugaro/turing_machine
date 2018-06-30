# Turing Machine
Turing Machine implemented in Python 3.x as a partial requirement in the course of Theory of computation.

## Execution
First is necessary converts the Turing machine file .jff, saved from a JFLAP 7.0, in a file .txt.
That is done by running the python script jflap-turing2utfpr.py:

```
$ python jflap-turing2utfpr.py <Input_file>.jff <output_file>.txt
```

Then executes the main.py file, giving the <output_file>.txt and the initial tape content of Turing machine:

```
$ python main.py <output_file>.txt <initial_tape_content>
```

If the turning computing reaches 500 iterations the program asks if you want to continue the computation. If 'y', 'Y', 's' or 'S' is given, the limit of iterations is doubled and the Turing computing continues otherwise the Turing computing is ended and prints every configuration in the queue.

# Files and classes

## file main.py

### Class Maincontroller
This class parses the input file, then create an instance of a Turing Machine. Also is responsible to access a validate method of
Turing machine and initialize your computing. After receiving the file, remove all leading and trailing characters of the line, transforms the line into a list. Then append the list in "file_content".


### main function
Validation of input file and creation of an instance of the Maincontroller class to perform execution.
So if the input format is valid then the calculation of the Turing machine is initialized.

## file turing_machine.py

### TuringMachine class
Executes a computation of Turing machine, in a way that applies this transition and puts in a queue every possible configuration and executes a transition of each configuration until you accept or reject the entry.
Checks if the machine attributes are correct with the function validate_input

## file tape.py

### Tape class
Simulates a tape of Turing machine. Has methods that simulate the movements of the tape (left, right or stay), reads and writes on the tape. When the reading head passes one of the extremities of the tape one blank symbol is added. This way the tape keep being infinite.
