from typing import List

def read_integers() -> List[int]:
    Integer = input()
    int_split = [int(x) for x in Integer.split(",")]
    return int_split

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())