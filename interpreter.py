from abc import ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):

    @abstractmethod
    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        self._expression.interpret()


class TerminalExpression(AbstractExpression):

    def interpret(self):
        pass


def main():
    abstract_syntax_tree = NonterminalExpression(TerminalExpression())
    abstract_syntax_tree.interpret()


if __name__ == '__main__':
    main()
