# Turing Machine
Turing Machine implemented in Python 3.x as partial requirement in the course of Theory of computation
   
## main.py  
  
### Class Maincontroller 
This class parses the input file, then create an instance of a Turing Machine. Also is responsible to access a validate method of
Turing machine and initialize your computing. After receiving the file, remove all leading and trailing characters of the line, transforms the line into a list. Then append the list in "file_content". 

  
### main function
Validation of input file and creation of an instance of the Maincontroller class to perform execution.
So if the input format is valid then the calculation of the Turing machine is initialized.

## turing_machine.py 

## tape.py 
The class tape simulates a tape of turing machine. Its operation simulates the movements of the tape: left, right or remain. He is also responsible for reading and writing on tape. When the head of the ribbon passes through one end then a white symbol is placed so that it remains an infinite tape.
