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

def test2():
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
    df.to_csv("output/test.csv", encoding="utf8", sep="\t")
    #~ anasem.pprint(result)
def test():
    import pprint
    text  =  u"يعبد الله منذ أن تطلع الشمس"
    result  =  []
    anasem  =  asm.SemanticAnalyzer()    
    result  =  anasem.analyze_text(text)    

    # the result contains objets
    sem_result = anasem.display_sem(result)
    pprint.pprint(sem_result)

def test_pprint():
    import pprint
    text  =  u"يعبد الله منذ أن تطلع الشمس"
    result  =  []
    anasem  =  asm.SemanticAnalyzer()    
    result  =  anasem.analyze_text(text)    

    # the result contains objets
    anasem.pprint(result)


def test_pd():
    import pprint
    text  =  u"يعبد الله منذ أن تطلع الشمس"
    result  =  []
    anasem  =  asm.SemanticAnalyzer()    
    result  =  anasem.analyze_text(text)    
    # the result contains objets
    df = pd.DataFrame(anasem.decode(result))
    print(df.head())
    df.to_csv("output/test.csv", encoding="utf8", sep="\t")

def test(display="pprint"):
    import pprint
    text  =  u"يعبد الله منذ أن تطلع الشمس"
    result  =  []
    anasem  =  asm.SemanticAnalyzer()    
    result  =  anasem.analyze_text(text)
    
    if display == "pandas":
        # the result contains objets
        df = pd.DataFrame(anasem.decode(result))
        print(df.head())
        df.to_csv("output/test.csv", encoding="utf8", sep="\t")
    elif display == "pprint":
        # the result contains objets
        anasem.pprint(result)        
    elif display == "only":
        # the result contains objets
        sem_result = anasem.display_sem(result)
        pprint.pprint(sem_result)      
    elif display == "all":
        # the result contains objets
        sem_result = anasem.display_sem(result, all=True)
        pprint.pprint(sem_result)
    else:
        pprint.pprint(result)


if __name__  ==  '__main__':
    #~ test2()
    #~ display_format = "all"
    #~ display_format = "pandas"
    display_format = "only"
    #~ display_format = "pprint"
    test(display_format)
