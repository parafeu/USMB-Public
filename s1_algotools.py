def average_above_zero(tab):
    """
    brief: computes the average ot the lists
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

#test script for fct average_above_zero
testTab=[1, 2, 3, -5] #create a fake tab
moy=average_above_zero(test_tab)
print('Positve values average = {val}'.format(val=moy))