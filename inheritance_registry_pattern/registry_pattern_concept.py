"""Typical structure of inheritance in OOP"""

from abc import ABC


class Car(ABC):
    """Below, pattern is shown. We can introduce any business logic with abstractmethod and run it recursively
    on subclasses as get_subs method is doing while aggregating all subclasses of given parent class.
    It has similarities to composite pattern but composite pattern is about creating given composite at runtime.
    Here we create create tree of inheritance without specifying it at runtime"""

    registry: dict = dict()

    @classmethod
    def __init_subclass__(cls, **kwargs):
        cls.registry: dict = dict()
        base_: Car
        for base_ in cls.__bases__:
            if hasattr(base_, "registry"):
                base_.registry[cls.__name__] = cls

    @classmethod
    def get_subs(cls) -> list:
        """Implement getting tree of subclasses using recursion"""
        return [{sub_name: sub_obj.get_subs()} for sub_name, sub_obj in cls.registry.items()]


class Bmw(Car):
    pass


class Series7(Bmw):
    pass


class E23(Series7):
    pass


class E32(Series7):
    pass


class E38(Series7):
    pass


class E65(Series7):
    pass


class F01(Series7):
    pass


class G11(Series7):
    pass


class Audi(Car):
    pass


class A3(Audi):
    pass


class A5(Audi):
    pass


class A6(Audi):
    pass


class A8(Audi):
    pass


if __name__ == "__main__":
    print(f"{Car.get_subs()= }")
    print(f"{Audi.get_subs()= }")
    print(f"{Series7.get_subs()= }")
