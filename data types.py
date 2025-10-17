# Python essential data types showcase
# Save as a .py file and run (Python 3)

def show(name, value):
    print(f"{name}: {value!r} (type: {type(value).__name__})")

# Basic scalar types
none_val = None
bool_val = True
int_val = 42
float_val = 3.14159
complex_val = 1 + 2j
str_val = "hello, world"

show("NoneType", none_val)
show("bool", bool_val)
show("int", int_val)
show("float", float_val)
show("complex", complex_val)
print(f" complex.real={complex_val.real}, complex.imag={complex_val.imag}\n")

# Binary sequences
bytes_val = b"byte\x00s"
bytearray_val = bytearray(b"mutable")
memoryview_val = memoryview(b"memoryview example")

show("bytes", bytes_val)
show("bytearray (before)", bytearray_val)
bytearray_val[0] = ord("M")  # modify mutable bytearray
show("bytearray (after)", bytearray_val)
show("memoryview (slice)", memoryview_val[0:6].tobytes())
print()

# Text sequence
show("str", str_val)
print(" str upper:", str_val.upper(), "\n")

# Sequence types
list_val = [1, 2, 3]
tuple_val = (1, 2, 3)
range_val = range(5)

show("list", list_val)
show("tuple", tuple_val)
show("range", range_val)
print(" range -> list:", list(range_val), "\n")

# Set types
set_val = {1, 2, 3}
frozenset_val = frozenset([1, 2, 3])

show("set", set_val)
show("frozenset", frozenset_val)
print()

# Mapping
dict_val = {"a": 1, "b": 2}
show("dict", dict_val)
print(" dict keys:", list(dict_val.keys()), "dict items:", list(dict_val.items()), "\n")

# Callables & objects
def example_function(x):
    return x * 2

class ExampleClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"ExampleClass({self.name!r})"

function_val = example_function
instance_val = ExampleClass("demo")

show("function", function_val)
show("class instance", instance_val)
print(" call function:", function_val(10), "\n")

# Generator (iterator) and comprehension
gen = (i * i for i in range(3))
list_comp = [i * 2 for i in range(3)]
dict_comp = {i: str(i) for i in range(3)}

show("generator (repr)", gen)
show("list comprehension", list_comp)
show("dict comprehension", dict_comp)
print(" generator -> list:", list(gen))