import sys


def check_card_validation(number_credit):
    # Declaration of variables
    copy_number = number_credit
    rem = 0
    sum = 0
    rem_aux = 0
    height = 0
    validation = ""

    # Sum numbers in odd position
    copy_number //= 10
    while copy_number != 0:
        # Picks the remainder (every odd position)
        rem = copy_number % 10
        # Goes to the other digit
        copy_number //= 100
        # Multiply the remainder by 2
        rem *= 2

        # If the remainder has more than 2 digits divide it
        if rem // 10 == 0:
            # Sums the remainder
            sum += rem
        else:
            # 1st digit
            rem_aux = rem % 10
            # Sums the remainder
            sum += rem_aux
            # 2nd digit
            rem_aux = rem // 10
            # Sums the remainder
            sum += rem_aux

    # Sum numbers in even position
    copy_number = number_credit
    while copy_number != 0:
        # Picks the remainder (every even position)
        rem = copy_number % 10
        # Goes to the other digit
        copy_number //= 100
        # Sums the remainder
        sum += rem

    # Reset the copy_number
    copy_number = number_credit
    # Call the lenHelper function to get the length
    height = lenHelper(copy_number)

    # All the conditions to check if the card is valid and what's the card's company
    # If the sum ends with a 0
    if sum % 10 == 0:
        # If the height is 13
        if height == 13:
            # If the number starts with 4, it is a VISA
            if copy_number // 1000000000000 == 4:
                validation = "VISA"
            else:
                validation = "INVALID"
        # If the height is 15
        elif height == 15:
            # If the number starts with 34 or 37, it is an AMEX
            if copy_number // 10000000000000 == 34 or copy_number // 10000000000000 == 37:
                validation = "AMEX"
            else:
                validation = "INVALID"
        # If the height is 16
        elif height == 16:
            # If the number starts with 4, it is a VISA
            if copy_number // 1000000000000000 == 4:
                validation = "VISA"
            # If the number starts with 5 and the second number is between 1 and 5, it is a MASTERCARD
            elif copy_number // 1000000000000000 == 5 and 1 <= (copy_number // 100000000000000) % 10 <= 5:
                validation = "MASTERCARD"
            else:
                validation = "INVALID"
        else:
            validation = "INVALID"
    else:
        validation = "INVALID"
    return validation


# Returns the number length
def lenHelper(number_card):
    if number_card >= 1000000000000000:
        return 16
    if number_card >= 100000000000000:
        return 15
    if number_card >= 1000000000000:
        return 13
    return 1


def main():
    try:
        # Ask to introduce the credit's card number
        number_credit = int(input("Number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        sys.exit(1)
    # Call the validation function to check if it's valid
    validation = check_card_validation(number_credit)
    # Prints the validation result
    print(validation)


if __name__ == "__main__":
    main()
