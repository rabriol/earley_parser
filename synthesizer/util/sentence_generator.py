__author__ = 'rafael-brito'

import math
import random


class SentenceGenerator(object):
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
            return [node.name.lower()]

        word = []
        for child in node.children:
            word += self.extract_sentences_from_tree(child)

        return word

    #responsable to generate the sentences
    @staticmethod
    def get_number_of_sentences(nodes, percent):
        return math.ceil(len(nodes) * (percent / 100))