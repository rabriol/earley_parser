# coding=utf-8

__author__ = 'rafaeuoliveira'

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
from synthesizer.service.earley_parser import EarleyParser
from synthesizer.util.generator import Generator
from synthesizer.model.result_test import ResultTest

if __name__ == '__main__':

    file_name = input("Por Favor, informa o diretorio do arquivo de córpus = ")
    number_of_testes = input("Por favor, informe o número de testes que deseja realizar = ")

    tests = []

    for test_number in range(number_of_testes):
        start = time.time()
        sentences, rules, lexicons = Generator().get_grammar_and_sentences(file_name)

        count_recognized = 0.00
        for sentence in sentences:
            recognized = EarleyParser().parse(rules, lexicons, sentence)
            if recognized:
                count_recognized += 1

        result_test = ResultTest(len(sentences), count_recognized, ((count_recognized / len(sentences)) * 100),
                                 (time.time() - start))

        tests.append(result_test)

    count_cobertura = 0.00
    index = 0
    for test in tests:
        index += 1
        count_cobertura += test.cobertura
        print '- ' * 35
        print '- ' * 35
        print 'TESTE NUMERO = %s' % index
        print 'Total de sentenças analisadas = %s' % test.total_sentences
        print 'Total de sentenças reconhecidas = %s' % test.total_recognized
        print 'Cobertura = %-5s' % test.cobertura
        print 'Tempo total de execução do teste = %-8s segundos' % test.total_time_elapsed
        print '- ' * 35
        print '- ' * 35

    #print "Média final da cobertura em relação aos %s testes realizados, foi de %s" & \
    #    number_of_testes, count_cobertura / number_of_testes