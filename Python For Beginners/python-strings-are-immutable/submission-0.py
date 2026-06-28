def remove_fourth_character(word: str) -> str:
    removing = word[:3]
    removing1 = word[4:8]
    new = removing+removing1
    return new

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
