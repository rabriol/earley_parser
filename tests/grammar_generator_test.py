#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

import unittest
from synthesizer.util.grammar_generator import GrammarGenerator
from synthesizer.util.extractor import Extractor


class GrammarGeneratorTest(unittest.TestCase):

    def test_generate_little_dict(self):
        corpus = '''(IP
            (VB Senhor))'''

        nodes = Extractor().init(corpus)
        rules, lexicons = GrammarGenerator().build_rules(nodes)

        self.assertTrue(['IP\n'] in rules['INITIAL'])
        self.assertTrue(['senhor'] in lexicons['VB'])

    def test_generate_little_bit_big_dict(self):
        corpus = '''(IP
            (NP (NPR Senhor))
            (. :)
            (VB Ofereço)
            (PP (P a)
                (NP (PRO$ Vossa)
                (NPR Majestade)))
            (NP (D as)
                (NPR Reflexões)
                (PP (P sobre)
                    (NP (D a)
                    (N vaidade)
                    (PP (P+D dos)
                        (NP (N homens))))))
            (. ;))'''

        corpus = corpus.replace('\t', '').replace('\r', '').replace('\n', '')
        nodes = Extractor().init(corpus)
        rules, lexicons = GrammarGenerator().build_rules(nodes)

        self.assertTrue(['NP', '.', 'VB', 'PP', 'NP', '.'] in rules['IP'])

        self.assertTrue(['senhor'] in lexicons['NPR'])
        self.assertTrue(['reflexões'] in lexicons['NPR'])
        self.assertTrue(['majestade'] in lexicons['NPR'])
        self.assertTrue(['dos'] in lexicons['P+D'])

    def test_generate_dict_from_file(self):
        nodes = Extractor().build_tree()
        rules, lexicons = GrammarGenerator().build_rules(nodes)

        self.assertTrue(['ADV', 'NP', 'VB', 'NP'] in rules['IP'])

    def test_get_little_grammar(self):
        corpus = '''(IP
            (NP Senhor))'''

        nodes = Extractor().init(corpus)

        grammar = GrammarGenerator().build_grammar(nodes)

        self.assertTrue(grammar)

    def test_get_grammar_from_file(self):
        nodes = Extractor().build_tree('/Users/rafaeuoliveira/Developer/workspace/python/synthesizer/resources/aires-treino.parsed')
        grammar = GrammarGenerator().build_grammar(nodes)

        self.assertTrue(grammar)