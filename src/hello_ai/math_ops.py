import numpy as np

def vector_length(x: list[float]) -> float :
    arr = np.array(x)
    return float(np.sqrt(np.sum(arr ** 2)))

def add_vectors(a: list[float], b: list[float]) -> list[float]:
    arr_a = np.array(a)
    arr_b = np.array(b)
    return (arr_a + arr_b).tolist()