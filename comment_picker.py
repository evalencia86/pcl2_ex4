#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Eva Bühlmann
# Sarah Kiener
#
# PCL II
# Übung 4 - Aufgabe 1.1

import bz2, json, gzip
from typing import BinaryIO


def mk_meme_corpus(infile: BinaryIO, outfile: str, min_score: int = 100, min_len: int = 1, max_len: int = 50):
    with gzip.open(outfile, 'wt', encoding='utf-8') as output:
        json_objects = iter_comments(infile, min_score, min_len, max_len)
        for json_object in json_objects:
            output.write(json_object)
            output.write('\n')


def iter_comments(stream, min_score, min_len, max_len):
    object_hashes = set()
    for element in stream:
        json_object = json.loads(element)  # aus Byte-Objekt ein json-dict machen
        comment = json_object['body']
        object_hash = hash(comment)
        if object_hash not in object_hashes:
            object_hashes.add(object_hash)
            upvotes = json_object['score']
            if upvotes >= min_score and min_len <= len(comment) <= max_len:
                yield comment


def main():
    with bz2.open('Korpusdaten/RC_2012-06.bz2', 'rb') as corp_file:
        mk_meme_corpus(corp_file, 'abstract_output/out_11.gz')


if __name__ == '__main__':
    main()

