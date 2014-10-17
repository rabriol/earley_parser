#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

import unittest
from synthesizer.util.grammar_generator import GrammarGenerator
from synthesizer.util.extractor import Extractor
from synthesizer.model.term import Term


class GrammarGeneratorTest(unittest.TestCase):

    def test_generate_little_dict(self):
        corpus = '''(IP
            (NP Senhor))'''

        nodes = Extractor().init(corpus)
        rules, lexicons = GrammarGenerator().build_rules(nodes)

        self.assertTrue([Term('IP\n')] in rules['INITIAL'])
        self.assertTrue([Term('senhor')] in lexicons['NP'])

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

        self.assertTrue([Term('NP'), Term('.'), Term('VB'), Term('PP'), Term('NP'), Term('.')] in rules['IP'])

        self.assertTrue([Term('senhor')] in lexicons['NPR'])
        self.assertTrue([Term('reflexões')] in lexicons['NPR'])
        self.assertTrue([Term('majestade')] in lexicons['NPR'])
        self.assertTrue([Term('dos')] in lexicons['P+D'])

    def test_generate_dict_from_file(self):
        nodes = Extractor().build_tree()
        rules, lexicons = GrammarGenerator().build_rules(nodes)

        self.assertTrue([Term('ADV'), Term('NP'), Term('VB'), Term('NP')] in rules['IP'])

    def test_get_little_grammar(self):
        corpus = '''(IP
            (NP Senhor))'''

        nodes = Extractor().init(corpus)

        grammar = GrammarGenerator().build_grammar(nodes)

        self.assertTrue(grammar)

    def test_get_grammar_from_file(self):
        nodes = Extractor().build_tree()
        grammar = GrammarGenerator().build_grammar(nodes)

        self.assertTrue(grammar)