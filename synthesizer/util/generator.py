#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

from synthesizer.util.sentence_generator import SentenceGenerator
from synthesizer.util.extractor import Extractor
from synthesizer.util.grammar_generator import GrammarGenerator


class Generator(object):
    @staticmethod
    def get_grammar_and_sentences(file_name=None):
        nodes = Extractor().build_tree(file_name)
        sentences, start_at, number_of_sentences = SentenceGenerator().get_sentences(nodes)
        #nodes_for_grammar = nodes[0:int(start_at)] + nodes[int(start_at+number_of_sentences):len(nodes)]
        rules, lexicons = GrammarGenerator().build_grammar(nodes)
        return sentences, rules, lexicons