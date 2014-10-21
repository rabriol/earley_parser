# coding=utf-8

__author__ = 'rafaeuoliveira'

import time
from synthesizer.service.earley_parser import EarleyParser
from synthesizer.util.generator import Generator

if __name__ == '__main__':

    input_read = input("Por Favor, informa o diretorio do arquivo de córpus = ")

    start = time.time()

    
    sentences, rules, lexicons = Generator().get_grammar_and_sentences(input_read)

    count_recognized = 0.00
    for sentence in sentences:
        recognized = EarleyParser().parse(rules, lexicons, sentence)
        if recognized:
            count_recognized += 1

    print '- ' * 35
    print 'Total de sentenças analisadas = %s' % len(sentences)
    print 'Total de sentenças reconhecidas = %s' % count_recognized
    print 'COBERTURA = %-5s' % ((count_recognized / len(sentences)) * 100)
    print 'Tempo total de execução do teste = %-8s segundos' % (time.time() - start)
    print '- ' * 35