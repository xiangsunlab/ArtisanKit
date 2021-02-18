#!/usr/bin/env python3
# plotting.py

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
"""ArtisanKit Plotting Canvas."""
import matplotlib as plt
def savefig(path,figname):
    '''
    path = path to save directory.
    figname = filename for figures, will be saved as figname.pdf and figname.png
    
    Usage example:
    -------------------
    >>> path = "../ArtisanKit/sample/Figures/"
    >>> figname ='Figure1'
    saved 1 .pdf file to ../ArtisanKit/sample/Figures/Figure1.pdf
    saved 1 .png file to ../ArtisanKit/sample/Figures/Figure1.png
    
    '''  
    # update future **kwargs to modify dpi, facecolor, etc.
    filename = ('{}/{}.pdf').format(path,figname)
    plt.savefig(filename,dpi=300,bbox_inches='tight',transparent=False) 
    print("saved 1 .pdf file to", filename)
    filename = ('{}/{}.png').format(path,figname)
    plt.savefig(filename,dpi=300,bbox_inches='tight',transparent=False,facecolor='white')
    print("saved 1 .png file to", filename);


class plotting:
    def __init__(self,parm1,parm2):
        self.parm1 = "x"
        self.parm2 = "y"
