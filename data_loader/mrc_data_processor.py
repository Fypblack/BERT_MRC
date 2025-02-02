#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


# Author: Xiaoy LI
# Description:
# mrc_ner_data_processor.py


import os
from data_loader.mrc_utils import read_mrc_ner_examples


class QueryNERProcessor(object):
    # processor for the query-based ner dataset 
    def get_train_examples(self, data_dir):
        data = read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.train"))
        return data

    def get_dev_examples(self, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.dev"))

    def get_test_examples(self, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.dev"))


class Conll03Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "PER", "LOC", "MISC", "O"]


class MSRAProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["NS", "NR", "NT", "O"]


class Onto4ZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["LOC", "PER", "GPE", "ORG", "O"]


class Onto5EngProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['ORDINAL', 'CARDINAL', 'LOC', 'WORK_OF_ART', 'LANGUAGE', 'ORG', 'FAC', 'PERSON', 'EVENT', 'TIME', 'LAW',
                'NORP', 'PERCENT', 'DATE', 'GPE', 'QUANTITY', 'PRODUCT', 'MONEY', 'O']


class ResumeZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "LOC", "NAME", "RACE", "TITLE", "EDU", "PRO", "CONT", "O"]


class GeniaProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['cell_line', 'cell_type', 'DNA', 'RNA', 'protein', "O"]


class ACE2005Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]


class ACE2004Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]


class CCKSProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["dis", "sym", "pro", "equ", "dru", "ite", "bod", "dep", "mic", "O"]


class CCKSTask2Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["试验要素", "性能指标", "任务场景", "系统组成", "O"]


class KGCovid19Processor(QueryNERProcessor):
    def get_labels(self, ):
        return [
            "Disease",
            "Phenotype",
            "Drug",
            "ChemicalCompound",
            "Gene",
            "Virus",
            "Organization",
            "Chemical",
            "O"
        ]
