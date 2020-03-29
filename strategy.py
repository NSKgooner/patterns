from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    """Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий некоторого алгоритма.
    Контекст использует этот интерфейс для вызова алгоритма, определенного Конкретными Стратегиями."""

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))


class Context:
    """Контекст определяет интерфейс, представляющий интерес для клиентов."""

    def __init__(self, strategy: Strategy) -> None:
        """Обычно Контекст принимает стратегию через конструктор,
        а также предоставляет сеттер для ее изменения во время выполнения."""
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """Контекст хранит ссылку на один из объектов Стратегии.
        Контекст не знает конкретного класса стратегии.
        Он должен работать со всеми стратегиями через интерфейс Стратегии."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        """Обычно контекст позволяет заменить объект стратегии во время выполнения."""
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """Вместо того чтобы самостоятельно реализовывать множественные версии алгоритма,
        Контекст делегирует некоторую работу объекту Стратегии."""
        result = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e'])
        print(','.join(result))


if __name__ == '__main__':
    context = Context(ConcreteStrategyA())
    context.do_some_business_logic()
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
