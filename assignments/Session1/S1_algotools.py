import random
import numpy as np

def average_above_zero(tab):
    """
    brief: computes the average of the lists
    Args: 
        tab: a list of numeric values, expects at least one positive values
    Return: 
        the computed average
    Raises: 
        ValueError if no positive value is found
    """

    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')

    average=-99
    valSum=0.0
    nPositiveValues=0

    for val in tab:
        if val > 0:
            valSum+=float(val)
            nPositiveValues+=1
    if nPositiveValues <= 0:
        raise ValueError('No positive value found')

    average=valSum/nPositiveValues

    return average

def max_value(tab):
    """
    brief: get the maximum value of the list
    Args: 
        tab: a list of numeric values, expects at least one positive values
    Return: 
        the maximum value of the list
        the index of maximum value
    Raises: 
        ValueError if no positive value is found
        ValueError if first argument is not a list
    """

    maxValue=0
    maxValueIndex=-99
    nPositiveValues=0
    i=0

    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')

    while i < len(tab):
        if tab[i] > 0:
            nPositiveValues+=1
            if tab[i] > maxValue:
                maxValue=tab[i]
                maxValueIndex=i
        i+=1
    if nPositiveValues <= 0:
        raise ValueError('No positive value found')
    
    return [maxValue, maxValueIndex]

def reverse_table(table):
    """
    brief: reverse a table
    Args: 
        table: a list of values
    Return: 
        the same list reversed
    Raises: 
        ValueError if first argument is not a list
    """

    if not(isinstance(table, list)):
        raise ValueError('Expected a list as input')

    listLen=len(table)
    loopMaxID=int(np.floor(listLen/2))
    listLen-=1
    for idx in range(loopMaxID):
        element=table[listLen-idx]
        table[listLen-idx]=table[idx]
        table[idx]=element
    
    return table

def roi_bbox(input_image):
    """
    brief: compute bounding box of a matrix
    Args: 
        input_image: a 2D matrix of booleans
    Return: 
        a numpy array of shape 4x2 filled with the four 2D coordinates
    Raises: 
        ValueError if first argument is not a matrix
        ValueError if matrix values are not booleans
    """

    if not(isinstance(input_image, np.ndarray)):
        raise ValueError('Expected a numpy 2d array')
    if not(input_image.dtype == np.bool):
        raise ValueError('Expected input of type boolean')

    minX=input_image.shape[0]
    maxX=0
    minY=input_image.shape[1]
    maxY=0

    for y in range(input_image.shape[0]):
        for x in range(input_image.shape[1]):
            if input_image[y, x]:
                if minY > y:
                    minY = y
                if maxY < y:
                    maxY = y
                if minX > x:
                    minX = x
                if maxX < x:
                    maxX = x

    return np.array([
        [minX, minY],
        [maxX, minY],
        [minX, maxY],
        [maxX, maxY]
    ])

def alea(v):
    """
    brief: return random value between 0 and v
    Args: 
        v: max random value (integer)
    Return: 
        a random integer
    Raises: 
        ValueError if v is not an integer
    """

    if not(isinstance(v, int)):
        raise ValueError('Expected an integer')
    
    return random.randint(0, v)

def random_fill_sparse(table, K):
    """
    brief: randomly fill table with X char K times
    Args: 
        table: a 2D array of char
        K: an integer
    Return: 
        the randomly fill table
    Raises: 
        ValueError if table is not a list
        ValueError if table value is not a list
        ValueError if K is not an integer
    """

    if not(isinstance(K, int)):
        raise ValueError('Expected an integer')
    
    if not(isinstance(table, list)):
        raise ValueError('Expected a list')
    
    randX=0
    randY=0

    i=0

    while(i <= K):
        randY=alea(len(table)-1)
        if not(isinstance(table[randY], list)):
            raise ValueError('Expected a list')
        randX=alea(len(table[randY])-1)
        table[randY][randX]='X'
        i+=1
    
    return table

# def remove_whitespace(table):
#     """
#     brief: remove whitespaces of a string
#     Args: 
#         table: a string
#     Return: 
#         the string without whitespaces
#     Raises: 
#         ValueError if table is not a string
#     """

#     if not(isinstance(table, str)):
#         raise ValueError('Expected a string')

#     i=0
#     table=list(table)

#     for cIndex, c in enumerate(table):
#         if c == ' ':
#             if cIndex == len(table) -1:
#                 table = table[:-1]
#             else:
#                 i=cIndex
#                 while i < len(table):
#                     table[cIndex] = table[cIndex+i]
#                     i+=1
#                 table = table[:-1]
    
#     return table       

#test script for fct average_above_zero
testTab=[1, 5, 3, -5] #create a fake tab
testBoundingBox=np.zeros((950, 850), dtype=np.bool)
testBoundingBox[2:4,3:5]=np.ones((2, 2), dtype=np.bool)
testBoundingBox[842:845,6:8]=np.ones((3, 2), dtype=np.bool)
testRandomFill=[
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
]
moy=average_above_zero(testTab)
max=max_value(testTab)
reverse_table(testTab)
boundingCoords=roi_bbox(testBoundingBox)
randomlyFill=random_fill_sparse(testRandomFill, 8)
print('Positive values average = {val}'.format(val=moy))
print('Max value = {val}, index = {id}'.format(val=max[0], id=max[1]))
print('Reversed table = {val}'.format(val=testTab))
print('Bounding box coordinates : {val}'.format(val=boundingCoords))
print('Randomly fill 2d table : ')
for filllist in randomlyFill:
    print(filllist)