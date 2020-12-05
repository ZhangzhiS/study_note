#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "黑桃 方块 梅花 红桃".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
