def divide(first, second):
    if second == 0:
        return "Ошибка"
    else:
        return first / second

def main():
    print(divide(10, 2))
    print(divide(5, 0))


if __name__ == "__main__":
    main()
