import validators;

def validate_string(value):
    if not validators.length(value, min=1):
        return False;

    return True;

def validate_int(value):
    if not validators.between(value, min=0):
        return False;
    
    return True;
    