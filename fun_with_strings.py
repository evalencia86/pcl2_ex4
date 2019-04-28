#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Eva Bühlmann
# 05-058-912
#
# PCL II
# Übung 4 - Aufgabe 2


from typing import Iterable


def longest_substrings(x: str, y: str) -> Iterable[str]:
    n = len(x)
    m = len(y)
    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    d[0][0] = 0
    for i in range(1, n + 1):
        d[i][0] = 0
    for j in range(1, m+1):
        d[0][j] = 0

    sub_dict = {}  # Dictionary mit Substrings. Key=Tuple mit Start-Koordinaten.
    max_sub_len = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1].lower() == y[j - 1].lower():
                d[i][j] = d[i - 1][j - 1] + 1
                if d[i][j] == 1:
                    sub_dict[(i, j)] = x[i - 1]
                    if d[i][j]>max_sub_len:
                        max_sub_len=d[i][j]
                else:
                    sub_dict[(i - d[i][j] + 1, j - d[i][j] + 1)] += x[i - 1]
                    if d[i][j]>max_sub_len:
                        max_sub_len=d[i][j]

    if not sub_dict:
        return None

    max_sublist = []
    for sub in sub_dict.values():
        if len(sub) == max_sub_len:
            max_sublist.append(sub)
    return max_sublist


def main():
    print(longest_substrings('Kleistermasse', 'Meisterklasse'))
    print(longest_substrings('Tod', 'Leben'))
    print(longest_substrings('Haus', 'Maus'))
    print(longest_substrings('mozart', 'mozzarella'))
    print(longest_substrings('keep the interface!', 'KeEp ThE iNtErFaCe!'))


if __name__ == '__main__':
    main()
