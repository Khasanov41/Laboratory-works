"""
task-1.py
Prints star rectangles.

(c) Хасанов Ислам, КЭ-101
"""
from toolkit import PrintSquare, PrintRectangle


if __name__ == '__main__':
    match input(f"  1 - PrintRectangle\n"
                f"  2 - PrintSquare\n"
                f"Enter the number: "):
        case "1":
            print("Selected PrintRectangle")
            print("Reading data from 'input.txt'...")
            try:
                with open("input.txt", "r") as data:
                    rectangle_size = tuple(map(int, data.readline().split()))
                    print(f"Rectangle size: {rectangle_size[0]}x{rectangle_size[1]}")

                    file_to_write = data.readline()
                    file_to_write = file_to_write.rstrip()
                    print(f"File name to write: {file_to_write}")

                    PrintRectangle(*rectangle_size, file_to_write)
                    print(" Done!")
            except FileNotFoundError:
                print("'input.txt' file not found.\n Termination...")
        case "2":
            try:
                print("Selected PrintSquare")
                print("Reading data from 'input.txt'...")
                with open("input.txt", 'r') as data:
                    square_size = int(data.readline())
                    print(f"Square size: {square_size}x{square_size}")

                    file_to_write = data.readline()
                    file_to_write = file_to_write.rstrip()
                    print(f"File name to write: {file_to_write}")

                    PrintSquare(square_size, file_to_write)
                    print(" Done!")
            except FileNotFoundError:
                print("'input.txt' file not found.\n Termination...")
        case _:
            print("Nothing is selected.\n Termination...")
