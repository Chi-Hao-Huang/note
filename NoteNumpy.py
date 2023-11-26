# -*- coding: utf-8 -*-
import numpy

# Arrays
    # 與list不同處為array內所有資料型態需一致
    
    numpy.array([1,2,3,4,5])
    numpy.array([1,2,3,4,5],float)

# shape
    The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
    
    (a). Using shape to get array dimensions
    
    my_1D_array = numpy.array([1, 2, 3, 4, 5])
    print(my_1D_array.shape)    
    > (5,)
    
    my_2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
    print(my_2D_array.shape)     
    > (3, 2)
    
    (b). Using shape to change array dimensions
    
    change_array = numpy.array([1,2,3,4,5,6])
    change_array.shape = (3, 2)
    print(change_array)      
    > [[1 2],[3 4],[5 6]]
    
# Transpose
    my_array = numpy.array([[1,2,3], [4,5,6]])
    print(numpy.transpose(my_array))
    > [[1 4], [2 5], [3 6]]
    
# Flatten
    my_array = numpy.array([[1,2,3], [4,5,6]])
    print(my_array.flatten())
    > [1 2 3 4 5 6]
    
# zeros; ones
    print(numpy.zeros((1,2)))                    #Default type is float
    > [[0. 0.]] 
    
    print(numpy.zeros((1,2), dtype = numpy.int)) #Type changes to int
    > [[0 0]]
    
# sum
    my_array = numpy.array([ [1, 2], [3, 4] ])
    print numpy.sum(my_array, axis = 0)         #Output : [4 6]
    print numpy.sum(my_array, axis = 1)         #Output : [3 7]
    print numpy.sum(my_array, axis = None)      #Output : 10
    print numpy.sum(my_array)                   #Output : 10
    
# prod
    my_array = numpy.array([ [1, 2], [3, 4] ])
    print numpy.prod(my_array, axis = 0)            #Output : [3 8]
    print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
    print numpy.prod(my_array, axis = None)         #Output : 24
    print numpy.prod(my_array)                      #Output : 24
    
# min
    my_array = numpy.array([[2, 5], [3, 7], [1, 3], [4, 0]])
    print numpy.min(my_array, axis = 0)         #Output : [1 0]
    print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
    print numpy.min(my_array, axis = None)      #Output : 0
    print numpy.min(my_array)                   #Output : 0
    
# max
    my_array = numpy.array([[2, 5], [3, 7], [1, 3], [4, 0]])
    print numpy.max(my_array, axis = 0)         #Output : [4 7]
    print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
    print numpy.max(my_array, axis = None)      #Output : 7
    print numpy.max(my_array)                   #Output : 7
    
# mean
    my_array = numpy.array([ [1, 2], [3, 4] ])
    print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
    print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
    print numpy.mean(my_array, axis = None)     #Output : 2.5
    print numpy.mean(my_array)                  #Output : 2.5
    
# var
    my_array = numpy.array([ [1, 2], [3, 4] ])
    print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
    print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
    print numpy.var(my_array, axis = None)      #Output : 1.25
    print numpy.var(my_array)                   #Output : 1.25
    
# std
    my_array = numpy.array([ [1, 2], [3, 4] ])
    print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
    print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
    print numpy.std(my_array, axis = None)      #Output : 1.11803398875
    print numpy.std(my_array)                   #Output : 1.11803398875
    
# dot
    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])
    print numpy.dot(A, B)       #Output : 11
    
# cross
    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])
    print numpy.cross(A, B)     #Output : -2
    
# inner
    A = numpy.array([0, 1])
    B = numpy.array([3, 4])
    print numpy.inner(A, B)     #Output : 4
    
# outer
    A = numpy.array([0, 1])
    B = numpy.array([3, 4])
    print numpy.outer(A, B)     #Output : [[0 0]
                                #          [3 4]]
# poly
    The poly tool returns the coefficients of a polynomial with the given sequence of roots.
    print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]

# roots
    The roots tool returns the roots of a polynomial with the given coefficients.
    print numpy.roots([1, 0, -1])           #Output : [-1.  1.]

# polyint
    The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
    print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5  1.  0.]

# polyder
    The polyder tool returns the derivative of the specified order of a polynomial.
    print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]

# polyval
    The polyval tool evaluates the polynomial at specific value.
    print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34

# polyfit
    The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
    print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
    #Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
    
# linalg.det
    The linalg.det tool computes the determinant of an array.
    print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

# linalg.eig
    The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
    vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
    print vals                                      #Output : [ 3. -1.]
    print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                    #          [ 0.70710678  0.70710678]]
# linalg.inv
    The linalg.inv tool computes the (multiplicative) inverse of a matrix.
    print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                    #          [ 0.66666667 -0.33333333]]
    
    
    
    
    
    
    
    
    