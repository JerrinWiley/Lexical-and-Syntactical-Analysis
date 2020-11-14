# Lexical-and-Syntactical-Analysis
A program that can evaluate arithmetic operators with integer numbers having any number of digits. The goal of this homework is to explore basic lexical and syntactic analysis.

program call: python3  infint.py "input=[input file name];digitsPerNode=[number of digits per node]" >> [output file name]
example: python3  infint.py "input=tc1.txt;digitsPerNode3" >> ans1.out

**** MY CODE IS BUILT TO HANDLE THE DIGITSPERNODE PARAMETER ****
I designed this program to accept a digits per node parameter, but it will use a default value of 3 if none is provided.

How the code works:
The program will take the given file name and read it to the program line by line. Each line will be checked for proper
formatting and sent to a solving function called nested_operations. This function operates similar to the demonstration
in class and sends the appropriate nested calculations to operator functions. Add will simply add the numbers together
starting with the least significant digit. Multiply uses an algorithm based on long multiplication and then adds
sub-answers back together. Finally the output is checked for length limits before it converted back to a string for
printing to console.
