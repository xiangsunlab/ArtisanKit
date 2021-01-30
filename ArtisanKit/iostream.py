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

# mypath = '/home/user/rundir/workdir/result'
# filepattern = '.dat'
# myfilepaths= survey(mypath, filepattern)

def survey(path,filepattern):
# Survey all files under path directory
    filepaths_ALL = []
    #Path = "/home/user/rundir/workdir"
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filepattern in filename:
                filepath = "{}/{}".format(dirpath,filename)
                filepaths_ALL.append(filepath)
    print("A total of ",len(filepaths_ALL),filepattern," files are detected")
    return filepaths_ALL
