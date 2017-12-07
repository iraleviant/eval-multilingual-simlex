"""
    This code computes the PPMI values for the raw co-occurrence matrix.
    PPMI values will be written to mat and it will get overwritten.
"""    
import numpy as np

def convertPPMI_original(mat):

    (nrows, ncols) = mat.shape
    colTotals = np.zeros(ncols, dtype=DTYPE)
    for j in range(0, ncols):
        colTotals[j] = np.sum(mat[:,j].data)
    print colTotals
    N = np.sum(colTotals)
    for i in range(0, nrows):
        row = mat[i,:]
        rowTotal = np.sum(row.data)
        for j in row.indices:
            val = np.log((mat[i,j] * N) / (rowTotal * colTotals[j]))
            mat[i,j] = max(0, val)
    return mat
