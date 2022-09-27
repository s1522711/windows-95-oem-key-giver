import random
import os

while True:
    x = random.randint(0, 4)

    List = ["24796-OEM-0014736-66386", "16595-OEM-0001695-96524", "15795-OEM-0001355-07757",
            "12095-OEM-0004226-12233", "12095-OEM-0004226-12233"]

    os.system('cls||clear')
    print("Enter q to quit")
    print("Enter y to get a windows 95 oem key")
    print("Do you want a windows 95 OEM key?")
    inp = input("Enter your selection here and press ENTER: ")

    if inp == "q":
        break

    if inp == "y":
        os.system('cls||clear')
        print(List[x])
        print("")
        input("press enter to continue...")
        os.system('cls||clear')

    else:
        os.system('cls||clear')
        print("Wrong!")
        print("")
        input("press enter to continue...")
        os.system('cls||clear')
