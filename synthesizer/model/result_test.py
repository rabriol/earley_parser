__author__ = 'rafaeuoliveira'


class ResultTest(object):
    def __init__(self, total_sentences, total_recognized, cobertura, total_time_elapsed):
        self.total_sentences = total_sentences
        self.total_recognized = total_recognized
        self.cobertura = cobertura
        self.total_time_elapsed = total_time_elapsed