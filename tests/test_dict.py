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
import unittest
import sys
sys.path.append('../asmai')    

sys.path.append('../')    
sys.path.append('../support')    

import qalsadi.analex     
import asmai.anasem as asm
import sylajone.anasyn
import sylajone.syn_const as syc   
import pyarabic.araby as araby

class asmaiTestCase(unittest.TestCase):
    """Tests for `asmai`."""
    def test_analyze(self):
        """ """
        analyzer = asm.SemanticAnalyzer()
        inpt =  ['كرة', 'القدم']
        output=u"كرة القدم"
        self.assertEqual(analyzer.analyze(inpt), output)
        
if __name__  ==  '__main__':
    unittest.main()
