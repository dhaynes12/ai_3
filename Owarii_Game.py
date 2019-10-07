

def GetWhoMovesFirst():
    while True:
        first = input("Who gets to move first ('s' or 'south' for south; 'n' or 'north' for north): ")
        first = first.lower()
        if first == 's' or first == 'south':
            return 0
        elif first == 'n' or first == 'north':
            return 1
        else:
            print("Improper input. Please try again.")


def main():
    print(GetWhoMovesFirst())

if __name__ == '__main__':
    main()
