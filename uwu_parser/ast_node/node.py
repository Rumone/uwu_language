from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, children=[]):
        self.children = children

    def __str__(self):
        return self.__class__.__name__ + '(' + ', '.join([str(node) for node in self.children]) + ')'

    @abstractmethod
    def evaluate_node(self):
        pass

