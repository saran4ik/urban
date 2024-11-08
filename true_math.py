from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second


def main():
    print(divide(6, 2))
    print(divide(3, 0))


if __name__ == "__main__":
    main()
