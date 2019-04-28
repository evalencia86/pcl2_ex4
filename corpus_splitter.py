#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Eva Bühlmann
# 05-058-912
#
# PCL II
# Übung 4 - Aufgabe 1.2


from typing import BinaryIO
from lxml import etree as ET
from pathlib import Path
import gzip, random


def split_corpus(infile: BinaryIO, targedir: str, n: int=1000):
    target = Path(targedir)
    corp_it = corpus_iterator(infile)

    double_selection = algo_r(corp_it, n*2)
    test_dev_set = algo_r(double_selection, n, keep_remaining=True)
    test_set = test_dev_set[0]
    dev_set = test_dev_set[1]

    infile.seek(0)  # reopen infile
    corp_it2 = (x for x in corpus_iterator(infile) if x not in double_selection)

    with gzip.open(target / 'abstracts.txt.training.gz', 'wt', encoding='utf-8') as train_file:
        for sent in corp_it2:
            train_file.write(sent)
            train_file.write('\n')

    with gzip.open(target / 'abstracts.txt.test.gz', 'wt', encoding='utf-8') as test_file:
        for sent in test_set:
            test_file.write(sent)
            test_file.write('\n')

    with gzip.open(target / 'abstracts.txt.development.gz', 'wt', encoding='utf-8') as dev_file:
        for sent in dev_set:
            dev_file.write(sent)
            dev_file.write('\n')


def algo_r(iterable, k, keep_remaining=False):
    reservoir = []
    remaining = []

    for i, item in enumerate(iterable):
        if i < k:
            reservoir.append(item)
        else:
            m = random.randint(0, i)
            if m < k:
                if keep_remaining:
                    remaining.append(reservoir[m])
                reservoir[m] = item
            elif keep_remaining:
                remaining.append(item)

    if keep_remaining:
        return reservoir, remaining
    else:
        return reservoir


def corpus_iterator(infile):  # BinaryIO):
    for _, element in ET.iterparse(infile, tag='document'):
        sentences = ' '.join(sentence.text for sentence in element.iterfind('.//sentence'))
        yield sentences
        element.clear()


def main():
    with gzip.open('Korpusdaten/abstracts.xml.gz', 'rb') as xml_file:
        split_corpus(xml_file, 'abstract_output')


if __name__ == '__main__':
    main()

