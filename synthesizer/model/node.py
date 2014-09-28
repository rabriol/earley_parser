__author__ = 'rafael-brito'


class Node(object):
    def __init__(self, name, children):
        self.name = name
        self.children = children
        
    def is_leaf(self):
        return self.children is None