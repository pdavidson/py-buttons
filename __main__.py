from src.Stoplight import Stoplight
from src.Bootstrapper import Bootstrapper


def main(args=None):
    print("Main Subroutine")
    Bootstrapper(Stoplight("abbabbc")).bootstrap()

    x = input()


if __name__ == "__main__":
    main()