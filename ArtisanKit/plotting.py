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
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

def savefig(path,figname):
    '''
    Parameters:
    -------------------
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
    print("saved 1 .png file to", filename)


class plotting:
    def __init__(self,parm1,parm2):
        self.parm1 = "x"
        self.parm2 = "y"

#From hands-on ML tutorial
def plot_dbscan(dbscan, X, size, show_xlabels=True, show_ylabels=True):
    core_mask = np.zeros_like(dbscan.labels_, dtype=bool)
    core_mask[dbscan.core_sample_indices_] = True
    anomalies_mask = dbscan.labels_ == -1
    non_core_mask = ~(core_mask | anomalies_mask)

    cores = dbscan.components_
    anomalies = X[anomalies_mask]
    non_cores = X[non_core_mask]
    
    plt.scatter(cores[:, 0], cores[:, 1],
                c=dbscan.labels_[core_mask], marker='o', s=size, cmap="Paired")
    plt.scatter(cores[:, 0], cores[:, 1], marker='*', s=20, c=dbscan.labels_[core_mask])
    plt.scatter(anomalies[:, 0], anomalies[:, 1],
                c="r", marker="x", s=100)
    plt.scatter(non_cores[:, 0], non_cores[:, 1], c=dbscan.labels_[non_core_mask], marker=".")
    if show_xlabels:
        plt.xlabel("$x_1$", fontsize=14)
    else:
        plt.tick_params(labelbottom=False)
    if show_ylabels:
        plt.ylabel("$x_2$", fontsize=14, rotation=0)
    else:
        plt.tick_params(labelleft=False)
    plt.title("eps={:.2f}, min_samples={}".format(dbscan.eps, dbscan.min_samples), fontsize=14)


#From hands-on ML tutorial
def plot_centroids(centroids, weights=None, circle_color='w', cross_color='k'):
    if weights is not None:
        centroids = centroids[weights > weights.max() / 10]
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='o', s=30, linewidths=8,
                color=circle_color, zorder=10, alpha=0.9)
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=50, linewidths=50,
                color=cross_color, zorder=11, alpha=1)

#From hands-on ML tutorial
def plot_gaussian_mixture(clusterer, X, resolution=1000, show_ylabels=True):
    mins = X.min(axis=0) - 0.1
    maxs = X.max(axis=0) + 0.1
    xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                         np.linspace(mins[1], maxs[1], resolution))
    Z = -clusterer.score_samples(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z,
                 norm=LogNorm(vmin=1.0, vmax=30.0),
                 levels=np.logspace(0, 2, 12))
    plt.contour(xx, yy, Z,
                norm=LogNorm(vmin=1.0, vmax=30.0),
                levels=np.logspace(0, 2, 12),
                linewidths=1, colors='k')

    Z = clusterer.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z,
                linewidths=2, colors='r', linestyles='dashed')
    
    plt.plot(X[:, 0], X[:, 1], 'k.', markersize=2)
    plot_centroids(clusterer.means_, clusterer.weights_)

    plt.xlabel("$x_1$", fontsize=14)
    if show_ylabels:
        plt.ylabel("$x_2$", fontsize=14, rotation=0)
    else:
        plt.tick_params(labelleft=False)