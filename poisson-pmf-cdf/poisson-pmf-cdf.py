import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    x=(math.exp(-lam)*(lam**k))/math.factorial(k)
    d={"pmf":x}
    s=0
    for i in range(k+1):
        s+=((math.exp(-lam)*(lam**i))/math.factorial(i))
    d["cdf"]=s
    return d