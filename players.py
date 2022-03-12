#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:09:16 2022

@author: chris
"""
from search import alpha_beta_search, expect_minmax
import random

def query_player(Game, state):
    """Make a move by querying standard input."""
    print("current state:")
    Game.display(state)
    print("available moves: {}".format(Game.actions(state)))
    print("")
    move = None
    if Game.actions(state):
        move_string = input('Your move? ')
        try:
            move = eval(move_string)
        except NameError:
            move = move_string
    else:
        print('no legal moves: passing turn to next player')
    return move


def random_player(Game, state):
    """A player that chooses a legal move at random."""
    return random.choice(Game.actions(state)) if Game.actions(state) else None


def alpha_beta_player(Game, state):
    return alpha_beta_search(state, Game)


def expect_min_max_player(Game, state):
    return expect_minmax(state, Game)