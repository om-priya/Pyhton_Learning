import ast, inspect, pprint
from abc import ABC, ABCMeta
import dis


class student(ABC):
    pass


class person(metaclass=ABCMeta):
    pass


def func():
    yield 1
    yield 2
    yield 3


def multi(*args):
    pass


def say():
    print("Hello")


pprint.pprint(ast.dump(ast.parse(inspect.getsource(multi))))
# pprint.pprint(ast.dump(ast.parse(inspect.getsource(person))))

# dis.dis(student)
# dis.dis(person)

dis.dis(multi)
print(multi.__code__.co_consts)
print(multi.__code__)
