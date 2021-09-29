from decimal import Decimal
from fractions import Fraction


def user_defined_function_example():
    # this is a function (not a method)
    pass


def generator_example():
    for i in range(10):
        yield i


class ClassExample:
    def __init__(self):
        pass

    def instance_method_example(self):
        # this is a method (not a function)
        pass


if __name__ == '__main__':
    print("---------- NUMBERS ----------")

    # Integral numbers
    print("Integral (Integer): %s" % type(1))
    print("Integral (Boolean): %s" % type(True))

    # Non-Integral numbers
    print("Non-Integral (Float): %s" % type(1.5))
    print("Non-Integral (Complex): %s" % type(complex(2, -3)))
    print("Non-Integral (Decimal): %s" % type(Decimal(1) / Decimal(7)))
    print("Non-Integral (Fraction): %s" % type(Fraction(1, 3)),  end="\n\n")

    print("---------- SEQUENCES ----------")

    # Mutable
    print("Mutable (Lists): %s" % type([1, 2, 3]))

    # Immutable
    print("Immutable (Strings): %s" % type("Hello world"))
    print("Immutable (Tuples): %s" % type((1, 3)),  end="\n\n")

    print("---------- SETS ----------")

    # Mutable
    print("Mutable (Sets): %s" % type({"a", 1, "z"})) # TODO: sets and frozen sets playground

    # Immutable
    print("Immutable (Frozen Sets): %s" % type(frozenset(("a", "e", "i", "o", "u"))),  end="\n\n")

    print("---------- DICTIONARY ----------")

    print("Dictionary (Dictionary): %s" % type({"hello": "world"}),  end="\n\n")

    print("---------- CALLABLES ----------")

    # User defined functions
    print("User defined functions (Function): %s" % type(user_defined_function_example))

    # Generators
    print("Generators (Generator): %s" % type(generator_example()))  # TODO: generators playground

    # Classes
    print("Classes (Type): %s" % type(ClassExample))

    # Instance method
    instance = ClassExample()
    print("Instance method (Method): %s" % type(instance.instance_method_example))

    # Built-in function
    print("Built-in functions (Builtin function or method): %s" % type(len))

    # Built-in method
    print("Built-in methods (Builtin function or method): %s" % type([].append),  end="\n\n")

    print("---------- SINGLETONS ----------")

    print("None (NoneType): %s" % type(None))
    print("Not implemented (NotImplemented): %s" % type(NotImplemented))  # TODO: NotImplemented playground
    print("Ellipsis (Ellipsis): %s" % type(...))  # TODO: slicing playground
