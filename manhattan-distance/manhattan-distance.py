import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    s=0
    for i in range(len(x)):
       s+=abs(x[i]-y[i])
    #print(type(s))
    return float(s)