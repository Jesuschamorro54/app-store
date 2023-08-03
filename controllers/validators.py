R = '\033[31m'  # Red
RS = '\033[39m'  # Reset
 
def num_validator(value, ref=0):
    
    if isinstance(value, (int, float)) and value >= ref: # Documentar despues.
        return True
    
    else:
        print(f"{R} * The value: {value} must be a positive number.{RS}")


def str_validator(value):

    if isinstance(value, (str)): # Documentar despues.
        return True

    else:
        print(f"{R} * The value: {value} must be a string.{RS}")

def bool_validator(value):

    if isinstance(value, (bool)):
        return True
    
    else:
        print(f"{R} * The value: {value} must be a boolean. {RS}")

