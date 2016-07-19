from src.Stoplight import Stoplight
from src.Bootstrapper import Bootstrapper


def main(args=None):
    print("Main Subroutine")
    # Bootstrapper(Stoplight("abbabbc")).bootstrap()

    my_array = []
    while True:
        x = raw_input()
        my_array.append(x)
        print my_array


if __name__ == "__main__":
    main()