#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

import unittest
from synthesizer.util.generator import Generator


class GeneratorTest(unittest.TestCase):

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