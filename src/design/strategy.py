from abc import ABCMeta, abstractmethod
from collections import Callable


class AbstractAction(metaclass=ABCMeta):
    def __init__(self, name, strategy):
        assert isinstance(strategy, Callable)
        self.name = name
        self.strategy = strategy

    @abstractmethod
    def info(self):
        pass


class ConcreteAction(AbstractAction):
    def info(self):
        print('{} is using strategy {}'.format(self.name, self.strategy))


def strategy_one():
    print('one')


def strategy_two():
    print('two')


if __name__ == '__main__':
    act1 = ConcreteAction('act1', strategy_one)
    act1.info()
    act1.strategy()

    act2 = ConcreteAction('act2', strategy_two)
    act2.info()
    act2.strategy()