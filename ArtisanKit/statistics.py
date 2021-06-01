#!/usr/bin/env python3
# statistics.py

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

"""ArtisanKit Statistical Toolbox."""
# For statistics and data analysis
import numpy as np
import scipy as sp
import pandas as pd
import math 
import matplotlib.pyplot as plt


def sort_and_index(df,column_name):
    """
    df : dataframe
    column_name : string , header of column to be sorted
    sort data
    """
    final_list=[]
    mylist= list(df[column_name])
    sorted_list = sorted(mylist,reverse=True)
    for i in sorted_list:
        a = mylist.index(i) + 1 # 1 because python index start from 0 and excited states = from 1 
        final_list.append(a)
    return final_list, sorted_list


def calc_pearson_coefficient(data, column_initial='D', print_result=False, corr_threshold=1e-2):
    """
    Calculate pearson coefficient between pairs of arrays
    column name should be initial + number 
    
    a summary statistics of the most correlated , least correlated are given and illustrated through plot.
    
    print_result : bool, 
        whether or not to print a full dataframe content, default = no 
        
    
    return 
    df, a data frame with name of variable A, B and the correlation between the two
    df_sorted, a sorted dataframe from largest to the lowerst value and its index
    """
    data_shape = data.shape
    data_length = data_shape[0]
    data_width = data_shape[1]
    desc_A =[]
    desc_B =[]
    pc=[]
    counter=[]
    count = 0
    for i in range(data_width):
        for j in range(data_width):
            myx = column_initial+str(i+1)
            myy = column_initial+str(j+1)
            if i!=j and j>i:
                count += 1
                my_rho = np.corrcoef(data[myx], data[myy])
                desc_A.append(myx)
                desc_B.append(myy)
                pc.append(my_rho[0][1]) # pick the off-diagonal element my_rho[0][1] = my_rho[1][0]
                counter.append(count)
                if print_result == True:
                    print('pearson correlation between ', myx ,' and ', myy,  ' is = ', my_rho[0][1])
                else:
                    continue
                    
    #create final dataframe of result            
    df = pd.DataFrame({'A': desc_A,
                      'B': desc_B,
                      'rho_c': pc})
    df_sorted = sort_and_index(df,column_name='rho_c')
    maxval=np.max(df['rho_c'])
    minval=np.min(df['rho_c'])
    abs_pc=np.abs(pc)
    nearzero= np.min(abs_pc)
    
            
    plt.scatter(counter,df['rho_c'],color = 'k' ,marker='o')
    plt.scatter(pc.index(maxval),maxval, color = 'b' ,marker='o')
    plt.scatter(pc.index(minval),minval, color = 'r' ,marker='o')
    plt.xlabel('Index', fontsize=16)
    plt.ylabel('Pearson Correlation', fontsize=16)
    
    print('Max value =', maxval, ' ; index = ', pc.index(maxval) , ' ; between ',desc_A[pc.index(maxval)] , ' and ',desc_B[pc.index(maxval)] )
    print('Min value =', minval, ' ; index = ', pc.index(minval), ' ; between ',desc_A[pc.index(minval)] , ' and ',desc_B[pc.index(minval)] )
    for i in pc:
        if abs(i - nearzero) < 1e-2:
            print('Least correlated values = ', i, ' ; index = ', pc.index(i), ' ; between ',desc_A[pc.index(i)] , ' and ',desc_B[pc.index(i)] )
            plt.scatter(pc.index(i),i, color = 'orange' ,marker='o')
            
    plt.show()
    return df ,df_sorted