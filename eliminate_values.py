from basiclayout import *
from replace_empty_with_alldigits import *
def eliminate(values):
    for s in values.keys():
        if len(values[s])==1:
            v=values[s]
            for peer in peers[s]:
                values[peer]=values[peer].replace(v,'')
    return(values)
values=eliminate(values)