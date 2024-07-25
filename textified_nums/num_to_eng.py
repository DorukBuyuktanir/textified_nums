def int_to_eng(input:int) -> str:
    '''
    NOT READY YET!!!
    Converts a integer number to text in English
    '''
    return "";

def float_to_eng(input:float) -> str:
    '''
    NOT READY YET!!!
    Converts a float number to text in English
    '''
    return "";

def num_to_eng(input) -> str:
    input = (input, type(input));
    if(input[1] == int):
        return int_to_eng(input[0]);
    elif(input[1] == float):
        return float_to_eng(input[0]);
    elif(input[1] == complex):
        print("Complex numbers are not supported yet...");
        return None;
    else:
        print("Unsupported type: Only integers ands floats are supported"
            + __name__);
        return None;