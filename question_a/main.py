

def check_overlap(line1: tuple, line2: tuple) -> bool:
    """
    Checks if there is  an overlap between two lines
    
    Params:
    - line1: A tuple containing the initial and the final points of the first line
    - line2: A tuple containing the initial and the final points of the second line
    
     Returns:
    - True if there is an overlap otherwise False
    """
    _first = list(line1)
    _second  = list(line2)
    #sorting the list so the order of the numbers in the tuples doesn't matter
    _first.sort()
    _second.sort()
    _first_range= range(*_first)
    _second_range= range(*_second)
        
    f = lambda x: x in _second_range
    result = list(filter(f, _first_range))
    return len(result) > 0
