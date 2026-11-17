import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a1=0
    b1=0
    ab=0
    for i in range(len(a)):
        ab+=a[i]*b[i]
        a1+=a[i]**2
        b1+=b[i]**2
    a1=a1**0.5
    b1=b1**0.5
    if a1==0 or b1==0:
        return 0.0
    return float(ab/(a1*b1))