__author__ = 'rafael-brito'

import unittest
from collections import deque
from synthesizer.util.extractor import Extractor
from synthesizer.model.node import Node


class TestConsumeNode(unittest.TestCase):
    
    #Solves (NPR Senhor)
    def test_build_basic_node_with_one_leaf(self):
        crts = deque(['N', 'P', 'R', ' ', 'S', 'e', 'n', 'h', 'o', 'r', ])
        node = Extractor().build_node(crts)
        
        self.assertEquals(node.name, 'NPR', 'os valores nao sao iguais')
        self.assertTrue(len(node.children) == 1, 'este no nao possui filho')
        self.assertEquals(node.children[0].name, 'Senhor', 'os valores nao sao iguais')

    #Solves (NP (NPR Senhor))
    def test_build_node_with_other_node_child(self):
        crts = deque(['N', 'P', ' ', Node('NPR', [Node('Senhor', None)])])
        node = Extractor().build_node(crts)
        
        self.assertEquals(node.name, 'NP', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].name, 'NPR', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].children[0].name, 'Senhor', 'os valores nao sao iguais')
    
    #Solves (IP (NP (NPR Senhor)) (. :))
    def test_build_node_with_two_children(self):
        node_npr = Node('NP', [Node('NPR', [Node('Senhor', None)])])
        node_dot = Node('.', [Node(':', None)])
        
        crts = deque(['I', 'P', ' ', node_npr, node_dot])
        node = Extractor().build_node(crts)
        
        self.assertEquals(node.name, 'IP', 'os valores nao sao iguais')
        
        self.assertEquals(node.children[0].name, 'NP', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].children[0].name, 'NPR', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].children[0].children[0].name, 'Senhor', 'os valores nao sao iguais')
        self.assertTrue(node.children[0].children[0].children[0].is_leaf(), 'nao e uma folha')
        
        self.assertEquals(node.children[1].name, '.', 'os valores nao sao iguais')
        self.assertEquals(node.children[1].children[0].name, ':', 'os valores nao sao iguais')
        self.assertTrue(node.children[1].children[0].is_leaf(), 'nao e uma folha')
        
    #Solves IP (NP (NPR Senhor)) (. :) (VB Ofereco))
    def test_build_complete_sentence_in_node(self):
        corpus = 'I (N s) (T a))'
        node, corpus = Extractor().crosser(corpus)
        
        self.assertEquals(node.name, 'I', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].name, 'N', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].children[0].name, 's', 'os valores nao sao iguais')
        self.assertTrue(node.children[0].children[0].is_leaf(), 'nao e uma folha')
        self.assertEquals(node.children[1].name, 'T', 'os valores nao sao iguais')
        self.assertTrue(node.children[1].children[0].is_leaf(), 'nao e uma folha')
        self.assertEquals(node.children[1].children[0].name, 'a', 'os valores nao sao iguais')
        
    def test_build_complete_big_sentence_in_node(self):
        corpus = 'IP (NP (NPR Senhor)) (. :) (VB Ofereco) (PP (P a) (NP (PRO Vossa) (NPR Majestade))) ' \
                 '(NP (D as) (NPR Reflexoes) (PP (P sobre) (NP (D a) (N vaidade) (PP (PD dos) (NP (N homens)))))) ' \
                 '(. ;))'

        node, corpus = Extractor().crosser(corpus)
        
        self.assertEquals(node.name, 'IP', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].name, 'NP', 'os valores nao sao iguais')
        self.assertTrue(len(node.children) == 6, 'a quantidade de children nao esta correto')
    
    def test_build_a_list_of_three_sentence(self):
        corpus_one = '(IP (NP (NPR Senhor)) (. :) (VB Ofereco) (PP (P a) (NP (PRO Vossa) (NPR Majestade))) ' \
                     '(NP (D as) (NPR Reflexoes) (PP (P sobre) (NP (D a) (N vaidade) (PP (PD dos) (NP (N homens))))' \
                     ')) (. ;))'
        corpus_two = '(CP (WADVP (WADV Quanto)) (IP (VB deram) (NP (D os) (N homens))) (, ,))'
        corpus_three = '(TA (CONJ e) (PP (P com) (NP (N vaidade))) (VB morremos) (. ;))'
        corpus = corpus_one + corpus_two + corpus_three
        
        nodes = Extractor().init(corpus)
        
        self.assertTrue(len(nodes) == 3, 'o tamanho da lista esta incorreto')
        self.assertEquals(nodes[0].name, 'IP', 'os valores nao sao iguais')
        self.assertEquals(nodes[1].name, 'CP', 'os valores nao sao iguais')
        self.assertEquals(nodes[2].name, 'TA', 'os valores nao sao iguais')
    
    def test_corpus_with_whiteespace(self):
        corpus = '  '
        nodes = Extractor().init(corpus)
    
        self.assertTrue(len(nodes) == 0)
    
    def test_build_from_string_not_well_formatted(self):
        corpus = """(IP (CONJ e)
        (PP  (P com)
          (NP (N vaidade)))
        (VB morremos)
        (. ;))"""
        
        nodes = Extractor().init(corpus)
        
        node = nodes[0]
        self.assertEquals(node.name, 'IP', 'os valores nao sao iguais')
        self.assertEquals(node.children[0].name, 'CONJ', 'os valores nao sao iguais')
        self.assertEquals(node.children[1].name, 'PP', 'os valores nao sao iguais')
        self.assertEquals(node.children[1].children[0].name, 'P', 'os valores nao sao iguais')
        self.assertEquals(node.children[1].children[0].children[0].name, 'com', 'os valores nao sao iguais')
        self.assertEquals(node.children[2].name, 'VB', 'os valores nao sao iguais')
        self.assertEquals(node.children[3].name, '.', 'os valores nao sao iguais')
    
    def test_part_of_corpus_failing(self):
        corpus = """(IP (NP (DEM isto))
                    (SR e)
                    (NP (D o)
                        (ADJ mesmo)
                        (CP  
                            (C que)
                            (IP 
                                (IP (VB oferecer)
                                       (PP (P em)
                                           (NP (D um)
                                           (ADJ pequeno)
                                           (N livro)))
                                       (NP (DEM aquilo)
                                           (CP (CP (WPP (P de)                                   
                                                      (WPRO que))                              
                                                   (IP 
                                                       (NP (D o)
                                                           (N mundo)
                                                           (Q todo))
                                                       (NP (SE se))                          
                                                       (VB compoe)))
                                               (, ,)
                                               (CONJP (CONJ e)
                                                  (CP (WNP (WPRO que)
                                                         )
                                                      (IP   
                                                          (NP (FP so)
                                                              (PRO Vossa)
                                                              (NPR Majestade))
                                                          (NEG nao)
                                                          (TR tem) 
                                                          (. :)                             
                                                          (NP (ADJ feliz)
                                                                 (N indigencia)))))
                                               (, ,)
                                               (CONJP (CONJ e)
                                                  (CP (WNP (WPRO que))
                                                      (IP 
                                                          (PP (FP so)
                                                              (P em)
                                                              (NP (PRO Vossa)
                                                              (NPR Majestade)))
                                                          (NP (SE se))
                                                          (VB acha))))))))))
                    (. .))"""
        
        nodes = Extractor().init(corpus)
        node = nodes[0]
        self.assertEquals(node.name, 'IP', 'os valores nao sao iguais')
    
    def test_build_tree_from_file(self):
        nodes = Extractor().build_tree('/Users/rafaeuoliveira/Developer/workspace/python/synthesizer/resources/aires-treino.parsed')
        
        self.assertTrue(len(nodes) == 1758, 'o tamanho da lista esta incorreto')