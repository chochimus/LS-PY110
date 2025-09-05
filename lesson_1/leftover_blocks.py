"""
input: integer for available blocks
output: integer for blocks left over after building the tallest possible valid structure

explicit:
    - blocks are cubes
    - top layer is a single block
    - block must be supported by 4 blocks beneath it
    - blocks can support more than one block in an upper layer
    - no gaps between blocks

implicit:
    - layer number correlates with blocks in a layer:
    - the number of blocks in a layer is layer number * layer number

questions:
    is there a limit on how many uppert blocks a lower block can support?

    

- algorithm

given a number of blocks, starting from 0
subtract number of blocks for layer from number of blocks remaining
increment current layer number
calculate number of blocks required for next layer by squaring current layer
determine blocks remaining is greater than or equal to blocks required for layer
 - if enough blocks:
    repeat from step 2
 - if not:
    return remaining number
"""

def calculate_leftover_blocks(n):
    layer = 0
    remaining_blocks = n
    required_blocks = (layer + 1) ** 2
    while remaining_blocks >= required_blocks:
        remaining_blocks -= required_blocks
        layer += 1
        required_blocks = (layer + 1) **2
    
    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0)