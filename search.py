from basiclayout import *
from replace_empty_with_alldigits import *
from eliminate_values import *
from only_choice import *
from reduce_puzzle import *
def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    values=reduce_puzzle(values)
    if(values is False):
        return False
    if all(len(values[s]) == 1 for s in boxes): 
        return values
    mini=20
    for box in boxes:
        if(len(values[box])>1):
            if(mini>len(values[box])):
                mini=len(values[box])
                i=box
    for x in values[i]:
        newsudoku=values.copy()
        newsudoku[i]=x
        ans=search(newsudoku)
        if ans:
            return ans
values=search(values)
if values:
    display(values)