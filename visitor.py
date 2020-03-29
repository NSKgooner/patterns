from abc import ABCMeta, abstractmethod
from typing import List


class Component(metaclass=ABCMeta):
    """
    Интерфейс Компонента объявляет метод accept, который в качестве аргумента
    может получать любой объект, реализующий интерфейс посетителя.
    """

    @abstractmethod
    def accept(self, visitor) -> None:
        pass


class ConcreteComponentA(Component):
    """
    Каждый Конкретный Компонент должен реализовать метод accept таким образом,
    чтобы он вызывал метод посетителя, соответствующий классу компонента.
    """

    def accept(self, visitor) -> None:
        """
        Обратите внимание, мы вызываем visitConcreteComponentA, что
        соответствует названию текущего класса. Таким образом мы позволяем
        посетителю узнать, с каким классом компонента он работает.
        """

        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        """
        Конкретные Компоненты могут иметь особые методы, не объявленные в их
        базовом классе или интерфейсе. Посетитель всё же может использовать эти
        методы, поскольку он знает о конкретном классе компонента.
        """

        return 'A'


class ConcreteComponentB(Component):
    """
    То же самое здесь: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor) -> None:
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return 'B'


class Visitor(metaclass=ABCMeta):
    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов. Сигнатура метода посещения позволяет посетителю
    определить конкретный класс компонента, с которым он имеет дело.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    Клиентский код может выполнять операции посетителя над любым набором
    элементов, не выясняя их конкретных классов. Операция принятия направляет
    вызов к соответствующей операции в объекте посетителя.
    """

    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)

