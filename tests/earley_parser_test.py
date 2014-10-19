#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

import unittest
from synthesizer.service.earley_parser import EarleyParser
from synthesizer.util.generator import Generator


class EarleyParserTest(unittest.TestCase):
    def test_predict(self):
        result = EarleyParser().parse({'INITIAL':[['AB', 'PA']], 'AB':[['V']]},
                                      {'V':[['é'], ['opá'], ['eita']], 'PA':[['amor']]},
                                      ['é', 'amor'])

        print result

    def test_union(self):
        print dict({'A':[2,3]}, **{'A':[3,4,5,6]})

    def test_predict_2(self):
        sentences, rules, lexicons = Generator.get_grammar_and_sentences()

        result = EarleyParser().parse(rules, lexicons, sentences[0])

        print result