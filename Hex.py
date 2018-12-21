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
_PRINTABLE_SET_ = {e for e in range(_MIN_PRINT_ASCII_, _MAX_PRINT_ASCII_ + 1)}



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
    while True:
        buffer = file_handle.read(_READ_BUFFER_SIZE_)
        buffer_size = len(buffer)
        if buffer_size == 0:
            break
        
        hex_l = []
        printables_l = []
		
        for i in range(buffer_size):
            ascii_as_int = buffer[i]
            character = chr(ascii_as_int)
            hex_l.append("{0:02X} ".format(ascii_as_int))
            if ascii_as_int in _PRINTABLE_SET_:
                printables_l.append(character)
            else:
                printables_l.append(".")

        padding_size = _READ_BUFFER_SIZE_ - buffer_size
        for i in range(padding_size):
            hex_l.append("   ")

        print("{:08X}  {} {}".format(offset, "".join(hex_l), 
		        "".join(printables_l)), flush=True)
        offset += _READ_BUFFER_SIZE_
	

	
################################################################################
# END
################################################################################
