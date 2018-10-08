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
    Raises: 
        ValueError if no positive value is found
    """

    maxValue=0
    nPositiveValues=0

    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')

    for val in tab:
        if val > 0:
            nPositiveValues+=1
            if val > maxValue:
                maxValue = val
    if nPositiveValues <= 0:
        raise ValueError('No positive value found')
    
    return maxValue


#test script for fct average_above_zero
testTab=[1, 2, 3, -5] #create a fake tab
moy=average_above_zero(testTab)
max=max_value(testTab)
print('Positive values average = {val}'.format(val=moy))
print('Max value = {val}'.format(val=max))