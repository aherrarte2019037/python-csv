import validators;

#Verificar que el valor sea cadena y tenga un carácter como mínimo
def validate_string(value):
    if not validators.length(value, min=1):
        return False;

    return True;

#Verificar que el valor sea de tipo entero y sea 0 como mínimo
def validate_int(value):
    if not validators.between(value, min=0):
        return False;
    
    return True;
    