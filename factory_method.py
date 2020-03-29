from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Класс Создатель объявляет фабричный метод, который должен возвращать объект класса Продукт.
    Подклассы Создателя обычно предоставляют реализацию этого метода.
    """

    @abstractmethod
    def factory_method(self):
        """
        Обратите внимание,
        что Создатель может также обеспечить реализацию фабричного метода по умолчанию.
        """

    def some_operation(self) -> str:
        """
        Также заметьте, что, несмотря на название, основная обязанность Создателя не заключается в создании продуктов.
        Обычно он содержит некоторую базовую бизнес-логику,
        которая основана на объектах Продуктов, возвращаемых фабричным методом.
        Подклассы могут косвенно изменять эту бизнес-логику,
        переопределяя фабричный метод и возвращая из него другой тип продукта.
        """

        product = self.factory_method()  # Получаем объект-продукт.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    """
    Обратите внимание, что сигнатура метода по-прежнему использует тип абстрактного продукта,
    хотя фактически из метода вовзращается конкретный продукт.
    Таким образом, Создатель может оставаться независимым от конкретных классов продуктов.
    """

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()


class Product(ABC):
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все конкретные продукты.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct2"


def client_code(creator: Creator):
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через его базовый интерфейс.
    Пока клиент продолжает работать с создателем через базовый интерфейс,
    вы можете передать ему любой подкласс создателя.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2")
    client_code(ConcreteCreator2())
