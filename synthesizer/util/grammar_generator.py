#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'rafaeuoliveira'


class GrammarGenerator(object):
    def build_grammar(self, nodes):
        rules, lexicons = self.build_rules(nodes)

        count_rules = 0
        for key in rules:
            count_rules += len(rules[key])

        count_lexicons = 0
        for key in lexicons:
            count_lexicons += len(lexicons[key])

        print 'Total de regras ==> ', count_rules
        print 'Total de léxicos ==> ', count_lexicons

        return rules, lexicons

    def build_rules(self, nodes):
        rules = {'INITIAL': []}
        lexicons = {}

        for node in nodes:
            terms = rules['INITIAL']
            term = node.name
            if [term] not in terms:
                terms.append([term])

            self.build_rules_helper(node.name, node.children, rules, lexicons)

        return rules, lexicons

    def build_rules_helper(self, name, children, rules, lexicons):
        if len(children) == 1 and children[0].is_leaf():
            if name in ['NP', 'WPP']:
                return

            try:
                lexicons[name]
            except KeyError:
                lexicons[name] = []

            term = children[0].name.lower()

            if [term] not in lexicons[name]:
                lexicons[name].append([term])
                return

        else:
            if name in ['VB']:
                return
            try:
                rules[name]
            except KeyError:
                rules[name] = []

            terms = []
            for node in children:
                terms.append(node.name)
                self.build_rules_helper(node.name, node.children, rules, lexicons)

            if terms not in rules[name]:
                if len(terms) == 1 and name == terms[0]:
                    pass
                else:
                    rules[name].append(terms)

