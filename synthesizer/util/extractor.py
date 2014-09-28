__author__ = 'rafael-brito'

import cStringIO
from collections import deque
from synthesizer.model.node import Node


class Extractor():
    def __init__(self):
        pass

    #it reads the file
    def build_tree(self):
        file_name = '/Users/rafaeuoliveira/Developer/workspace/python/synthesizer/resources/aires-treino.parsed'
        data = open(file_name, 'r').read(60000000)
        stream = cStringIO.StringIO(data)
        
        corpus = stream.getvalue().replace('\t', '').replace('\r', '').replace('\n', '')
        
        nodes = self.init(corpus)
        
        return nodes

    #responsable to start the tree extract process
    def init(self, corpus):
        nodes = []
        corpus = corpus.strip()
        corpus_size = len(corpus)
        index = 0
        
        try:
            corpus[0]
        except IndexError:
            return nodes
        
        while not len(corpus) == 0:
            if not corpus_size == len(corpus):
                corpus_size = len(corpus)
                index = 0
        
            if corpus[index] == '(':
                node, corpus = self.crosser(corpus[index+1:])
                nodes.append(node)
            
            index += 1
            
        return nodes

    #responsable to detect when a new '(' appears to call a new recursion
    def crosser(self, corpus):
        corpus = corpus.strip()
        deque_c = deque()
        index = 0
        corpus_size = len(corpus)
        
        while not len(corpus) == 0:
            if not corpus_size == len(corpus):
                corpus_size = len(corpus)
                index = 0
            
            if corpus[index] == '(':
                if not len(deque_c) == 0 and not deque_c[-1] == ' ':
                    deque_c.append(' ')
                
                node, corpus = self.crosser(corpus[index+1:])
                deque_c.append(node)
            
            elif corpus[index] == ')':
                node = self.build_node(deque_c)
                
                try:
                    return node, corpus[index+1:]
                except Exception:
                    return node, None
            
            elif not len(deque_c) == 0 and isinstance(deque_c[0], Node):
                return deque_c, corpus[index:]
            
            elif not len(deque_c) == 0 and deque_c[-1] == ' ' and corpus[index] == ' ':
                pass
            else:
                deque_c.append(corpus[index])
            
            index += 1
        
        raise Exception('Error on Node construction')

    #responsable to detect when ')' appears and it builds a new Node()
    @staticmethod
    def build_node(deq):
        head_is_complete = False
        head = ''
        tail = ''
        child = []
        
        try:
            while deq:
                element = deq.popleft()
                if element == ' ' and head_is_complete is False:
                    head_is_complete = True
                elif not head_is_complete:
                    head += element
                elif head_is_complete and isinstance(element, basestring):
                    tail += element
                elif head_is_complete and isinstance(element, Node):
                    child.append(element)
                else:
                    pass
            
            if not len(child) == 0:
                node = Node(head, child)
            else:
                node = Node(head, [Node(tail, None)])
            return node
        except Exception:
            raise Exception('Error when building a Node, deq=' + str(deq) + 'head=' + str(head) + 'tail=' + str(tail))