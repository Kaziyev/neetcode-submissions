def divide_numbers(a: str, b: str) -> None:
    try:
        convert1 = int(a)
        convert2 = int(b)
        result = convert1/convert2
        print(result)
    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")