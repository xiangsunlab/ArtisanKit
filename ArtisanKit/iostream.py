#!/usr/bin/env python3
# iostream.py

#------------------------------------------------------------------------------------------------#
# This software was written in 2021/01                                                           #
# by Dominikus Brian <dominikusbrian@nyu.edu>/<dominikusbrian@live.com>  ("the author"),         #                    #
#                                                                                                #
# LICENCE                                                                                        #
# Creative Commons CC0 Public Domain Dedication.                                                 #
# To the extent possible under law, the author have dedicated all copyright and related          #
# and neighboring rights to this software to the PUBLIC domain worldwide.                        #
# This software is distributed without any warranty.                                             #
# You should have received a copy of the CC0 Public Domain Dedication along with this software.  #
# If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.                               #
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
