import torch

def tensor_info(x: list[float]) -> dict:
    tensor = torch.tensor(x, dtype=torch.float32)
    return {
        "tensor": tensor,
        "shape": tensor.shape,
        "dtype": tensor.dtype,
        "sum": float(tensor.sum()),
        "mean": float(tensor.mean())
    }

def add_tensors(a: list[float], b: list[float]) -> torch.Tensor:
    t1 = torch.tensor(a, dtype=torch.float32)
    t2 = torch.tensor(b, dtype=torch.float32)
    return t1 + t2