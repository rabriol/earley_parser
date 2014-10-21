#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'

import unittest
import time
from synthesizer.service.earley_parser import EarleyParser
from synthesizer.util.generator import Generator
from synthesizer.model.state import State


class EarleyParserTest(unittest.TestCase):
    def test_recognize_1(self):
        recognized = EarleyParser().parse({'INITIAL': [['AB', 'PA']], 'AB': [['V']]},
                                          {'V': [['é'], ['opá'], ['eita']], 'PA': [['amor']]},
                                          ['é', 'amor'])

        self.assertTrue(recognized)

    def test_recognize_2(self):
        """(IP
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
                (. ;))
        '"""

        rules = {'INITIAL': [['IP']],
                 'IP': [['NP', '.', 'VB', 'PP', 'NP', '.']],
                 'NP': [['NPR'], ['D', 'NPR', 'PP'], ['N'], ['PRO$', 'NPR'], ['D', 'N', 'PP']],
                 'PP': [['P', 'NP', 'NPR'], ['P', 'NP'], ['P+D', 'NP']]}

        lexicons = {'NPR': [['senhor'], ['majestade'], ['reflexões']], '.': [[':'], [';']],
                    'VB': [['ofereço']], 'P': [['a'], ['sobre']], 'PRO$': [['vossa']],
                    'D': [['as'], ['a']], 'N': [['vaidade'], ['homens']], 'P+D': [['dos']]}

        sentence = ['senhor', ':', 'ofereço', 'a', 'vossa', 'majestade', 'as', 'reflexões', 'sobre', 'a',
                    'vaidade', 'dos', 'homens', ';']

        recognized = EarleyParser().parse(rules, lexicons, sentence)

        self.assertTrue(recognized)

    def test_recognize_3(self):
        """
        (IP (NP (D a)
            (N natureza))
        (VB quer)
        (CP (C que)
            (IP
                (NP (CL nos))
                (VB amemos)))
        (, ,))
        """

        sentences, rules, lexicons = Generator.get_grammar_and_sentences()

        sentence = ['a', 'natureza', 'quer', 'que', 'nos']

        recognized = EarleyParser().parse(rules, lexicons, sentence)

        self.assertTrue(recognized)

    def test_recognize_from_all_corpus(self):
        sentences, rules, lexicons = Generator.get_grammar_and_sentences()

        start = time.time()

        count_recognized = 0.00
        for sentence in sentences:
            recognized = EarleyParser().parse(rules, lexicons, sentence)
            if recognized:
                count_recognized += 1

        print 'COBERTURA = %-4s' % ((count_recognized/len(sentences))*100)

        print 'Tempo total de execução do teste = %-8s' % (time.time() - start)

    def test_union(self):
        print dict({'A': [2, 3]}, **{'A': [3, 4, 5, 6]})

    def test_add_new_state(self):
        s = set()

        s.add(State('mm', ['A', 'B'], 0, None))
        s.add(State('mm', ['A', 'B'], 0, None))

        self.assertTrue(len(s) == 1)