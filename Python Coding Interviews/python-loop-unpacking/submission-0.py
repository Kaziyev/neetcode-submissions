from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max_score = -1
    names = ""
    for point in scores:
        x,y = point[0], point[1]
        if y>max_score:
            max_score = y
            names = x

    return names
        


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
