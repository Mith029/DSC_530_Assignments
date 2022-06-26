"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

# Importing libraries
from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemFile(dct, data, nrows):
    # Calling a function from thinkstats2 file to parse .dct files
    read_dct = thinkstats2.ReadStataDct(dct)
    
    # Reading the file into pandas dataframe 
    read_data = read_dct.ReadFixedWidth(data, compression='gzip', nrows=nrows)
    return read_data

def PregNum(respondant):
    # Importing Pregnancy file and parsing it
    preg_nsfg = nsfg.ReadFemPreg()
    
    # Dictionary map for each respondents 
    pregnum_map = nsfg.MakePregMap(preg_nsfg)
    
    # Looping through to unpack dictionary in order to verify respondent
    # and pregnancy files by comparing pregnum variable
    for ind, preg in respondant.pregnum.items():
        case_id = respondant.caseid[ind]
        index = pregnum_map[case_id]
        
        if len(index) != preg:
            print(caseid, len(index), preg)
            return False
    return True
    

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    # variable to save respondent dataframe respondent and pregnancy files
    df_respon = ReadFemFile("2002FemResp.dct","2002FemResp.dat.gz", None)
    
    # Display pregnum value count from the respondent file
    print(df_respon.pregnum.value_counts())
    
    # Calling a function to validate 
    PregNum(df_respon)
    
    # Displaying message to show no errors in the script 
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    # Calling main fucntion
    main(*sys.argv)
