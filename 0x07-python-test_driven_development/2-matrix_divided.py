#!/usr/bin/python3


def matrix_divided(matrix, div):
    """matrix_divided: function that divides all elements of a matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if type(div) is not float and type(div) != int:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    quot = [matrix[0], matrix[1]]
    return [[round(x / div, 2) for x in y] for y in matrix]
