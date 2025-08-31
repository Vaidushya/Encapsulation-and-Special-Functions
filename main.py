class my_class:

    __privatevar = 27

    def __private_meth(self):
        print("I'm inside my class room.")
    def hello(self):
        print(f"Private variable value: {my_class.__privatevar}")

foo = my_class()
foo.hello()
foo.__private_meth