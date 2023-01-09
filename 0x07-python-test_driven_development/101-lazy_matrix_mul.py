#!/usr/bin/python3

"""defines a function that multiplies 2 matrices using numpy"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """represents the function lazy_matrix_mul that multiplies matices using numpy
    m_a represents the first matrix
    m_b represnts the second matrix
    """

    return (np.matmul(m_a, m_b))
