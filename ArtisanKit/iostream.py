#!/usr/bin/env python3
# iostream.py

#------------------------------------------------------------------------------------------------#
# This software was written in 2021/01                                                           #
# by Dominikus Brian <dominikusbrian@nyu.edu>/<dominikusbrian@live.com>  ("the author"),         #                    #
#                                                                                                #
# GNU GENERAL PUBLIC LICENSE                                                                     #
# Version 3, 29 June 2007                                                                        #
#                                                                                                #   
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>                           #
# Everyone is permitted to copy and distribute verbatim copies                                   #
# of this license document, but changing it is not allowed.                                      #   
#                                                                                                #
# DISCLAIMER                                                                                     #
# The authors and publishers make no warranties about the software, and disclaim liability       #
# for all uses of the software, to the fullest extent permitted by applicable law.               #
#------------------------------------------------------------------------------------------------#

"""ArtisanKit I/O Stream Module."""

# Importing dependencies

import os 
import dask.dataframe as dd
import pickle as pkl


def survey(path,filepattern):
    '''
    Survey all files under path directory
    
    Usage example:
    -------------------
    >>> mypath = '../ArtisanKit/sample'
    >>> filepattern = '.dat'
    >>> myfilepaths= survey(mypath, filepattern)
    A total of  3 .dat  files are detected

    >>> myfilepaths
    ['../ArtisanKit/sample/test1.dat',
     '../ArtisanKit/sample/test2.dat',
     '../ArtisanKit/sample/test3.dat']

    >>> filelist
    ['test1.dat', 'test2.dat', 'test3.dat']

    '''
    filepaths_ALL = []
    file_with_pattern = []
    for root,dirs,files in os.walk(path):
        #print(dirnames) dirnames is part of the os.walk() trio
        for filename in files:
            if filepattern in filename:
                filepath = "{}/{}".format(root,filename)
                mypattern = "{}".format(filename)
                filepaths_ALL.append(filepath)
                file_with_pattern.append(mypattern)
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS metadata directories
    print("A total of ",len(filepaths_ALL),filepattern," files are detected")
    return filepaths_ALL, file_with_pattern

def print_dec(before,answer,after,dec):
    '''
    before = anything before scalar value
    answer = scalar values with many decimals you want to truncate
    after = anything after scalar value
    dec = the number of decimal points you want to show
    Usage example
    ------------------------------------------------------------
    >>> myvalue = 1.23829342
    >>> print("This is normal printing " ,myvalue )
    >>> print_dec("This print only 4 decimal points", myvalue , ",not bad right?", 4) 
    This is normal printing  1.23829342

    This print only 4 decimal points 1.2383 ,not bad right?.
    ------------------------------------------------------------
    print_dec("Give me 4 point decimals", 1.23829342, "so it is 4 decimals now", 4)
    : introduces the format spec
    0 enables sign-aware zero-padding for numeric types
    .number sets the precision to a "point" amount of decimal 
    f displays the number as a fixed-point number
    '''
    point = str(dec)
    formatter = "\n" + before + " {:0." + point + "f} " + after + "\n"
    print(formatter.format(answer))
