__author__ = 'rafael-brito'

import math
import random
from synthesizer.util.extractor import Extractor


class Generator():
    def __init__(self):
        pass

    def get_grammar_and_sentences(self):
        nodes = Extractor().build_tree()

        sentences, start_at, number_of_sentences = self.get_sentences(nodes)
        #grammar = self.get_grammar(nodes, start_at, number_of_sentences)

        return sentences

    #responsable to generate the grammar
    def get_grammar(self, nodes, start_at, sentence_number):
        grammar = None

        for node in nodes[0:int(start_at)] + nodes[int(start_at+sentence_number):len(nodes)]:
            #self.build_rules(node, grammar)
            pass

        return grammar

    #responsable to generate the sentences
    @staticmethod
    def get_number_of_sentences(nodes, percent):
        return math.ceil(len(nodes) * (percent / 100))

    def get_sentences(self, nodes):
        #retrive the total number of sentences that should be created
        sentence_number = self.get_number_of_sentences(nodes, 20.00)

        #retrieve a random index
        start_at = random.randint(1, len(nodes) - sentence_number)

        sentences = []
        for node in (nodes[int(start_at):int(start_at+sentence_number)]):
            sentence = self.extract_sentences_from_tree(node)
            sentences.append(sentence)

        return sentences, start_at, sentence_number

    def extract_sentences_from_tree(self, node):
        if node is None:
            return ''

        if node.is_leaf():
            return [node.name]

        sentences = []
        for child in node.children:
            sentences = sentences + self.extract_sentences_from_tree(child)

        return sentences