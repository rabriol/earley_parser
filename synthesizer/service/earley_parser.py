# coding=utf-8
__author__ = 'rafaeuoliveira'

import time
from synthesizer.model.column import Column
from synthesizer.model.state import State


class EarleyParser(object):
    def parse(self, rules, lexicons, sentence):
        start = time.time()

        chart = [Column(index, token) for index, token in enumerate([None] + sentence)]
        chart[0].add(State('ALPHA', ['INITIAL'], 0, chart[0]))

        rules_with_lexicons = dict(rules, **lexicons)

        for index, column in enumerate(chart):
            #esta variável evita vários predicts para um mesmo termo
            predicts_done = set()

            for state in column.states:
                if state.completed():
                    self.complete(column, state, rules_with_lexicons)
                else:
                    term = state.next_term()
                    if term in rules_with_lexicons:
                        if not term in predicts_done:
                            predicts_done.add(term)
                            self.predict(column, term, rules_with_lexicons)
                    elif index + 1 < len(chart):
                        self.scan(chart[index + 1], state, term)

        print '- ' * 35
        print 'Sentença = [%s] ' % (' '.join(sentence))

        recognized = False
        for st in chart[-1].states:
            if st.name == 'ALPHA' and st.completed():
                print '- ' * 35
                print 'RECONHECIDA!'
                recognized = True

        if recognized:
            #imprime o conjunto de estados completos que foram usados para reconhecer a sentença
            print '- ' * 35
            for ch in reversed(chart):
                for st in ch.states:
                    if st.completed():
                        print st
            print '- ' * 35
        else:
            print 'NÃO RECONHECIDA!'

        print 'Tempo total de execução => %-8s' % (time.time() - start)

        return recognized

    @staticmethod
    def predict(column, term, rules):
        for production in rules[term]:
            column.add(State(term, production, 0, column))

    @staticmethod
    def scan(column, state, term):
        if column.token == term:
            column.add(State(state.name, [column.token], state.dot_index + 1, state.start_column))

    @staticmethod
    def complete(column, state, rules_with_lexicons):
        if not state.completed():
            return
        for stat in state.start_column.states:
            term = stat.next_term()
            if not term in rules_with_lexicons:
                continue
            if term == state.name:
                column.add(State(stat.name, stat.production, stat.dot_index + 1, stat.start_column))

