#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

import unittest
from synthesizer.model.node import Node
from synthesizer.util.extractor import Extractor
from synthesizer.util.generator import Generator


class GeneratorTest(unittest.TestCase):

    def test_generate_sentences_of_20_percent(self):
        number = Generator().get_number_of_sentences([1,2,3,4,5,6,7,8,9,10], 20.00)
        self.assertEquals(number, 2, 'o calculo feito esta errado')

    def test_generate_sentences(self):
        number = Generator().get_number_of_sentences([1,2,3,4,5,6,7,8,9,10, 11], 20.00)
        self.assertEquals(number, 3, 'o calculo feito esta errado')

    def test_walk_in_tree(self):
        node = Node('IP',[Node('VB',
                               [Node('Declamei', None)]),
                          Node('PP',
                               [Node('P',
                                     [Node('contra', None),
                                      Node('NP',
                                           [Node('D',
                                                 [Node('a', None)]
                                           )]
                                      )]
                               )]
                          )]
                )

        sentence = Generator().extract_sentences_from_tree(node)

        self.assertEquals(['Declamei', 'contra', 'a'], sentence)

    def test_walk_in_tree_2(self):
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

        nodes = Extractor().init(corpus)

        sentence = Generator().extract_sentences_from_tree(nodes[0])

        self.assertEquals(['Senhor', ':', 'Ofereço', 'a', 'Vossa', 'Majestade', 'as', 'Reflexões', 'sobre', 'a',
                           'vaidade', 'dos', 'homens', ';'], sentence)

    def test_get_sentences(self):
        sentences = Generator().get_grammar_and_sentences()

        self.assertEquals(len(sentences), 352, 'a quantidade de sentencas retornada esta incorreta')

    '''(VB (AD amamos) (B de))
    def test_build_grammar(self):
        node = Node('VB', [Node('AD', [Node('amamos', None)]), Node('B', [Node('de', None)])])

        rule = Generator().build_rules(node)

        self.assertEquals(rule.name, 'VB', 'o nome da regra na eh o mesmo do esperado')
        self.assertEquals(rule.productions[0].terms[0].name, 'AD', 'o nome da regra na eh o mesmo do esperado')
        self.assertEquals(rule.productions[0].terms[0].productions[0].terms[0], 'amamos', 'o nome da regra na eh o mesmo do esperado')
        self.assertEquals(rule.productions[0].terms[1].name, 'B', 'o nome da regra na eh o mesmo do esperado')
        self.assertEquals(rule.productions[0].terms[1].productions[0].terms[0], 'de', 'o nome da regra na eh o mesmo do esperado')
    '''
