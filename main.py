print("Hello Orion - your ai environment is alive.")
from src.hello_ai.core import greet

greet()

from src.hello_ai.math_tools import double
print(double(21))

from src.hello_ai.math_ops import vector_length, add_vectors

print("length of vector [3,4]:", vector_length([3,4]))
print("adding vectors [1,2] and [3,4]:", add_vectors([1,2], [3,4]))