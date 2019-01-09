#! /usr/bin/env python

################################################################################
# FILE        : Hex.py
# DESCRIPTION : Outputs in hexadecimal form the contents of any given file
# AUTHOR      : M H Khaliq
# LICENSE     : MIT
################################################################################



################################################################################
# IMPORTS
################################################################################

import argparse



################################################################################
# CONSTANTS
################################################################################

_READ_BUFFER_SIZE_ = 16

_MIN_PRINT_ASCII_ = 0x20
_MAX_PRINT_ASCII_ = 0x7e
_NUM_ASCII_CHARS_ = 256
_UNPRINTABLE_CASE_ = "."



################################################################################
# MAIN
################################################################################

parser = argparse.ArgumentParser(
        description="Show contents of named file in hexadecimal form")
parser.add_argument("-f", "--file", metavar="FILE", help="File to read",
        required=True, dest="filename")
argsH = vars(parser.parse_args())

with(open(argsH["filename"], mode="rb")) as file_handle:
    offset = 0
	
    hex_a = []
    print_a = []
    for i in range(_NUM_ASCII_CHARS_):
        hex_a.append("{0:02X} ".format(i))
        if i >= _MIN_PRINT_ASCII_ and i <= _MAX_PRINT_ASCII_:
            print_a.append(chr(i))
        else:
            print_a.append(_UNPRINTABLE_CASE_)
	
    while True:
        buffer = file_handle.read(_READ_BUFFER_SIZE_)
        buffer_size = len(buffer)
        if buffer_size == 0:
            break
        
        hex_l = []
        printables_l = []
		
        for b in buffer:
            hex_l.append(hex_a[b])
            printables_l.append(print_a[b])
        
        if buffer_size < _READ_BUFFER_SIZE_:
            padding_size = _READ_BUFFER_SIZE_ - buffer_size
            for i in range(padding_size):
                hex_l.append("   ")

        print("{:08X}  {} {}".format(offset, "".join(hex_l), 
		        "".join(printables_l)), flush=True)
        offset += _READ_BUFFER_SIZE_
	

	
################################################################################
# END
################################################################################
