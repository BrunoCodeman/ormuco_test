
def check_values(val1:str, val2:str):
    try:
        _first = float(val1)
        _second = float(val2)
        _rel = "equals"
        _greater = _first
        _smaller = _second
        
        if _first > _second:
            _greater, _rel, _smaller = (_first, ">", _second)
        
        if _first < _second:
            _greater, _rel, _smaller = (_second, ">", _first)

        msg = f"{_greater} {_rel} {_smaller}"
    except ValueError as verr:
        #print(verr)
        msg = "gimme numbers plz"
    finally:
        return msg
    
    