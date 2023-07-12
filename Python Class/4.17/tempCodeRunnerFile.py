import copy

# Mutable object (list of strings)
original_list = ["hello", "world"]
shallow_copy_list = copy.copy(original_list)

shallow_copy_list[0] = "hi"

print(original_list)          # Output: ["hi", "world"]
print(shallow_copy_list)       # Output: ["hi", "world"]

