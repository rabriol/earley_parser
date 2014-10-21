#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

import unittest
from synthesizer.util.generator import Generator


class GeneratorTest(unittest.TestCase):

    def test_get_sentences(self):
        sentences, rules, lexicons = Generator().get_grammar_and_sentences('/Users/rafaeuoliveira/Developer/workspace/python/synthesizer/resources/aires-treino.parsed')

        self.assertEquals(len(sentences), 352, 'a quantidade de sentencas retornada esta incorreta')