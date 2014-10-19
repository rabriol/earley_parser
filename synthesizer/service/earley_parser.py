__author__ = 'rafaeuoliveira'

from synthesizer.model.column import Column
from synthesizer.model.state import State


class EarleyParser(object):
    def parse(self, rules, lexicons, sentence):
        chart = [Column(index, token) for index, token in enumerate([None] + sentence)]

        chart[0].add(State('ALPHA', ['INITIAL'], 0, chart[0]))

        rules_with_lexicons = dict(rules, **lexicons)

        for index, column in enumerate(chart):
            for state in column.states:
                if state.completed():
                    self.complete(column, state, rules_with_lexicons)
                else:
                    term = state.next_term()
                    if term in rules_with_lexicons:
                        self.predict(column, term, rules_with_lexicons)
                    elif index + 1 < len(chart):
                        self.scan(chart[index + 1], state, term)

        for f in chart[-1]:
            if f.name == 'ALPHA' and f.completed():
                return f

        raise Exception("Erro no parse")

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

