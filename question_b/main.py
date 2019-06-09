
def check_values(val1:str, val2:str) -> str:
    """
    Checks which value is greater

    Params:
    - val1: A string containing a number
    - val2: A string containing a number

    Returns:
    - A string with a message about which value is greater or if they are the same

    Excepts:
    - ValueError: Returns a message warning at least one of the parameters is not a number
    """
    
    try:
        _first = float(val1)
        _second = float(val2)
        _rel = "equals"
        _left_hand = _first
        _right_hand = _second
        
        if _first > _second:
            _left_hand, _rel, _right_hand = (_first, ">", _second)
        
        if _first < _second:
            _left_hand, _rel, _right_hand = (_second, ">", _first)

        msg = f"{_left_hand} {_rel} {_right_hand}"
    except ValueError as verr:
        msg = "gimme numbers plz"
    finally:
        return msg
    
    