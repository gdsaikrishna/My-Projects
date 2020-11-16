'''
Calculating Mean, Standard Deviation , median , mode , Confidence Interval for given list of Integers 
'''

'''
import pandas as pd
import numpy as np
from scipy import stats

n = int(input())
a = np.array(input().split())
a = a.astype(np.int32)

mean = np.mean(a)
sigma = np.std(a)
medi = np.median(a)
mod = stats.mode(a)
ci = stats.norm.interval(0.950004, loc=mean, scale=sigma/np.sqrt(n))
print("%.1f"%mean)
print("%.1f"%medi)
print("%.0f"%mod[0][0])
print("%.1f"%sigma)
print("%.1f %.1f"%(ci[0],ci[1]))
'''

#Bot Saves Princess

'''
3
---
-m-
p--           Path from m to p
'''

'''
def displayPathtoPrincess(n,grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))
    
    # negative row difference implies UP
    # negative col difference implies LEFT
    drows = princess[0] - mario[0]
    dcols = princess[1] - mario[1]

    print(''.join([
        'UP\n' * abs(drows) if drows < 0 else 'DOWN\n' * drows,
        'LEFT\n' * abs(dcols) if dcols < 0 else 'RIGHT\n' * dcols]))

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
'''