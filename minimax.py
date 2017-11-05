#!/usr/bin/python
#
# Copyright 2017 KiKe. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from minimax_helpers import *


# Solution using an explicit loop based on max_value()
def _minimax_decision(game_state):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """
    best_score = float("-inf")
    best_move = None
    for m in game_state.get_legal_moves():
        v = min_value(game_state.forecast_move(m))
        if v > best_score:
            best_score = v
            best_move = m
    return best_move


# This solution does the same thing using the built-in `max` function
# Note that "lambda" expressions are Python's version of anonymous functions
def minimax_decision(game_state):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """
    # The built in `max()` function can be used as argmax!
    return max(game_state.get_legal_moves(),
               key=lambda m: min_value(game_state.forecast_move(m)))
