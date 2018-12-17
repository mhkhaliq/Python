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

with(open(argsH["filename"], mode="rb")) as fh:
    offset = 0
    while True:
        buffer = fh.read(_READ_BUFFER_SIZE_)
        buffer_size = len(buffer)
        if buffer_size == 0:
            break
        
        hex_s = ""
        printables_s = ""
        for i in range(buffer_size):
            a = buffer[i]
            c = chr(a)
            hex_s += "{0:02X} ".format(a)
            if a in _PRINTABLE_SET_:
                printables_s += c
            else:
                printables_s += "."

        padding_size = _READ_BUFFER_SIZE_ - buffer_size
        for i in range(padding_size):
            hex_s += "   "

        print("{:08X}  {} {}".format(offset, hex_s, printables_s), flush=True)
        offset += _READ_BUFFER_SIZE_
	

	
################################################################################
# END
################################################################################
