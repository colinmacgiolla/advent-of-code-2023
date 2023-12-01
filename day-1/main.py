#!/bin/python


def calculate_calibration(text):
    if len(text) > 0:
        value = ''.join(i for i in text if i.isdigit())
        if len(value) < 2:
            value = int(''.join([value,value]))
        elif len(value) > 2:
            value = int(''.join([value[0],value[-1]]))
        else:
            value = int(value)
        return value
    else:
        return


def replace_text_numbers_in_stream(text):
    number_mapping = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven':'s7n',
        'eight':'e8t',
        'nine': 'n9e',
        'zero': 'z0o'
    }

    for word, replacement in number_mapping.items():
        text = text.replace(word, replacement)

    return text

def main():
    '''

    '''
    with open('.//day-1//input//data.txt') as f:
        raw_input = f.read()
        
    calibration = []
    for line in raw_input.split('\n'):
        result = calculate_calibration(line)
        if result is not None:
            calibration.append( result )
    
    print(f"Part 1: Sum of all values is: {sum(calibration)}")
    calibration.clear()
    for line in raw_input.split('\n'):
        update = replace_text_numbers_in_stream(line)
        result = calculate_calibration(update)
        if result is not None:
            calibration.append( result )
    print(f"Part 2: Sum of all values is: {sum(calibration)}")
    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
