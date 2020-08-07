#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_dict.py
#  
#  Copyright 2018 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )

import sys
import os.path
from io import open
import argparse
import pprint

sys.path.append('../')    

import asmai.anasem as asm

def grabargs():
    parser = argparse.ArgumentParser(description='Test Asmai analyzer.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=False,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-o", dest="outfile", nargs='?', 
        help="Output file to convert", metavar="OUTFILE")
    parser.add_argument("-c", dest="command", nargs='?', default="test",
        help="Command to run (test, generate, eval)", metavar="COMMAND")
    parser.add_argument("--limit", type=int, nargs='?',default = 1000,
                        help="Limit line to treat", metavar="LIMIT")
    args = parser.parse_args()
    return args


def main():
    args = grabargs()
    command = args.command
    limit = args.limit
    infile = args.filename
    outfile = args.outfile
    print(command, limit, infile, outfile)
    #~ sys.exit()    
    if infile:
        try:
            fl = open(infile, encoding="utf8")
        except:
            print("Can't open file ", infile)
            sys.exit()
    lines = fl.readlines()
    # create semantic analyzer object
    anasem  =  asm.SemanticAnalyzer()    
    for line in lines:
        text = line.strip()
        result  =  anasem.analyze_text(text)    
        sem_result = anasem.display_sem(result)
        print('*'*25)
        print('input: ', text)
        pprint.pprint(sem_result)


if __name__  ==  '__main__':
    #~ test2()
    main()
