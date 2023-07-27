height = 0


def main():
    global height
    height = check_height(height)
    draw_pyramids()


def check_height(height):
    while height < 1 or height > 8:
        try:
            height = int(input("Height: "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return height


def draw_pyramids():
    # Declaration and assignment of the character we're going to use for the pyramid.
    hashtag = '#'

    # Loop for the lines
    for rows in range(height):
        # Loop for the spaces in each row at the start.
        for spaces in range(height - rows - 1):
            print(" ", end='')

        # Loop for the left part of the pyramid.
        for left_rows in range(rows + 1):
            print(hashtag, end='')

        # Spaces in between
        print("  ", end='')

        # Loop for the right part of the pyramid.
        for right_rows in range(rows + 1):
            print(hashtag, end='')

        # New line
        print()


main()
