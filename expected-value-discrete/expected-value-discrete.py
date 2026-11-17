import numpy as np

def expected_value_discrete(x: list, p: list) -> float:

    x = np.array(x)
    p = np.array(p)

    return float(np.sum(x * p))
