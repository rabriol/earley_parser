__author__ = 'rafaeuoliveira'


class Term(object):
    def __init__(self, name, is_terminal=False):
        self.name = name
        self.is_terminal = is_terminal

    def __eq__(self, other):
        return self.name == other.name