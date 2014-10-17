__author__ = 'rafaeuoliveira'

from synthesizer.util.sentence_generator import SentenceGenerator
from synthesizer.util.extractor import Extractor
from synthesizer.util.grammar_generator import GrammarGenerator


class Generator(object):
    @staticmethod
    def get_grammar_and_sentences():
        nodes = Extractor().build_tree()

        sentences, start_at, number_of_sentences = SentenceGenerator().get_sentences(nodes)

        nodes_for_grammar = nodes[0:int(start_at)] + nodes[int(start_at+sentence_number):len(nodes)]

        grammar = GrammarGenerator().build_grammar(nodes_for_grammar)

        return sentences