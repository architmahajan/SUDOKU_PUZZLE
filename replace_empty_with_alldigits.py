from basiclayout import *
grid='4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
def grid_values(grid):
    d={}
    l=[]
    alldigits='123456789'
    for i in grid:
        if i=='.':
            l.append(alldigits)
        else:
            l.append(i)
    assert len(l)==81
    return dict(zip(boxes,l))
values=grid_values(grid)
print(grid)