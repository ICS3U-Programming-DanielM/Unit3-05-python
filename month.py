# Created by: Daniel Momoh
# Created on: Sep 2022
# This program allows user to insert a number and /n
# it would print the month that corresponds to the number /n


from calendar import month


def main():
    # input
    month = input("Enter the number of the month : ")
    print("")

    # process & output
    match month:
        case "1":
            print("The number represents January!")
        case "2":
            print("The number represents  February!")
        case "3":
            print("The number represents March!")
        case "4":
            print("The number represents April!")
        case "5":
            print("The number represents May!")
        case "6":
            print("The number represents June!")
        case "7":
            print("The number represents July!")
        case "8":
            print("The number represents August!")
        case "9":
            print("The number represents September!")
        case "10":
            print("The number represents October!")
        case "11":
            print("The number represents November!")
        case "12":
            print("The number represents December!")
        case _:
            print("The number does not represent a month")


if __name__ == "__main__":
    main()
