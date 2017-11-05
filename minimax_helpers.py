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


def terminal_test(game_state):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return not bool(game_state.get_legal_moves())


def min_value(game_state):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(game_state):
        return 1  # by Assumption 2
    v = float("inf")
    for m in game_state.get_legal_moves():
        v = min(v, max_value(game_state.forecast_move(m)))
    return v


def max_value(game_state):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(game_state):
        return 1  # by Assumption 2
    v = float("inf")
    for m in game_state.get_legal_moves():
        v = min(v, max_value(game_state.forecast_move(m)))
    return v
