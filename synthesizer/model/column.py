__author__ = 'rafaeuoliveira'


class Column(object):
    def __init__(self, index, token):
        self.index = index
        self.token = token
        self.states = []
        self.__unique = set()

    def __iter__(self):
        return iter(self.states)

    def __str__(self):
        return str(self.index)

    def add(self, state):
        if state not in self.__unique:
            self.__unique.add(state)
            state.end_column = self
            self.states.append(state)