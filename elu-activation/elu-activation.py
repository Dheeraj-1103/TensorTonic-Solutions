import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    r=[]
    for i in x:
        if i>0:
            r.append(i)
        else:
            r.append(alpha*((math.exp(i))-1))
    return r