def test_function():
    print("Я в области видимости module_4_2.py")

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # в рамках test_function() она запускается


test_function()

# inner_function() # функция не найдена, т.к. она внутри функции test_function()
