# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:11:49 2020

@author: Windows
"""
import numpy as np
import matplotlib as plt

def scale_diagonal(matrix):
    for i in range(25):
        matrix[i, i] = matrix[i, i] / 2.0
        
    return matrix



def uppertriangle_to_symmetric(matrix):
    matrix_trans = matrix.T
    matrix = matrix + matrix_trans
    matrix = scale_diagonal(matrix)
    
    return matrix

print uppertriangle_to_symmetric(obs_mu_ab)




#Heatmap

delta_mu = obs_sym - mu_ab

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
bx = fig.add_subplot(2, 2, 2)
cx = fig.add_subplot(2, 2, 3)

scale = max([abs(min(np.concatenate(delta_mu))), abs(max(np.concatenate(delta_mu)))])

MX1 = ax.mathshow(obs_sym, vmin = 0, vmax = 516)
MX2 = bx.matshow(mu_ab, vmin = 0, vmax = 516)
diffMX = cx.matshow(delta_mu, cmap= 'seismic', vmin = scale, vmax = scale)

plt.colorbar(MX1, ax = ax)
plt.colorbar(MX2, ax = bx)
plt.colorbar(diffMX, ax = cx)
plt.show()


