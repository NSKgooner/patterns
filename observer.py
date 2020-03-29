from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observer(ABC):
    """Интерфейс наблюдателя объявляет метод уведомления,
    который издатели используют для оповещения своих подписчиков."""

    @abstractmethod
    def update(self, subject):
        """Получить обновление от субъекта."""
        pass


class Subject(ABC):
    """Интерфейс издателя объявляет набор методов для увправления подписчиками."""

    state: int = None  # состояние Издателя, необходимое всем подписчикам
    _observers: List[Observer] = []  # список Подписчиков

    @abstractmethod
    def attach(self, observer: Observer):
        """Присоединяет наблюдателя к издателю."""
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """Отсоединяет наблюдателя от издателя."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Уведомляет всех наблюдателей о событии."""
        pass


class ConcreteSubject(Subject):
    """Издатель владеет некоторым важным состоянием и опопвещает наблюдателей о его изменениях."""

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """Запуск обновления в каждом подписчике."""
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """Обычно логика подписки - только часть того, что делает Издатель.
        Издатели часто содержат некоторую важную бизнес-логику, которая запускает метод уведомления всякий раз, когда должно произойти что-то важное (или после этого)."""

        self.state = randrange(0, 10)
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject.state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state == 0 or subject.state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == '__main__':
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    subject.some_business_logic()
    subject.some_business_logic()
    subject.detach(observer_a)
    subject.some_business_logic()

