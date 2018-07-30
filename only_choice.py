from basiclayout import *
from replace_empty_with_alldigits import *
from eliminate_values import *
def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

values=only_choice(values)