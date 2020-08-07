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
import functools
import operator
import pandas as pd

import qalsadi.analex     
import pyarabic.araby as araby

sys.path.append('../')    
sys.path.append('../asmai')    
sys.path.append('../support')    

import asmai.anasem as asm
import aranasyn.anasyn
import aranasyn.syn_const as syc

def functools_reduce(a):
    return functools.reduce(operator.concat, a)

def test():
    import pprint
    text  =  u"يعبد الله منذ أن تطلع الشمس"
    result  =  []
    analex  =  qalsadi.analex.Analex()
    anasyn  =  aranasyn.anasyn.SyntaxAnalyzer()
    anasem  =  asm.SemanticAnalyzer()    
    result  =  analex.check_text(text)
    result, synodelist  =  anasyn.analyze(result)
    # semantic result
    result  =  anasem.analyze(result)    

    # the result contains objets
    df = pd.DataFrame(anasem.decode(result))
    print(df.head())
    df.to_csv("output/test.csv", sep="\t")
    #~ anasem.pprint(result)
if __name__  ==  '__main__':
    test()
