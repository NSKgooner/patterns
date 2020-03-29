class SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному.
    Возможные способы включают в себя базовый класс, декоратор, метакласс.
    Мы воспользуемся метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")