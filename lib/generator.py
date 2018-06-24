# ************************************************************************* #
# This file is part of Shard.                                               #
#                                                                           #
# Shard is free software: you can redistribute it and/or modify             #
# it under the terms of the GNU Affero General Public License as            #
# published by the Free Software Foundation.                                #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              #
# GNU Affero General Public License for more details.                       #
#                                                                           #
# You should have received a copy of the GNU Affero General Public License  #
# along with this program. If not, see <http://www.gnu.org/licenses/>.      #
# ************************************************************************* #

import random
from copy import copy
from .parser import Rule, Token, Node

# ************************************************************************* #

def get_random_unicode() -> str:
    """
    http://stackoverflow.com/a/21666621
    """

    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]

    return random.choice(alphabet)

# ************************************************************************* #

def get_random_other() -> str:
    """
    http://stackoverflow.com/a/21666621
    """

    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]

    return random.choice(alphabet)

# ************************************************************************* #

def generate_token(token: Token, limit: int = 1000) -> str:
    """
    Generate token string.
    """

    res = []
    stack = [token.rule]

    while len(stack) > 0 and len(stack) < limit:
        item = stack.pop()

        if isinstance(item, Rule):

            if len(item.rules) == 0:
                raise RuntimeError("Incomplete rule '{}' specification".format(item.name))

            # Choose one rule
            items = random.choice(item.rules)

            items = items.copy()
            items.reverse()
            stack = stack + items
        else:
            if item == "UTF8_CHAR":
                c = get_random_unicode()
                res.append(c)
            elif item == "OTHER_CHAR":
                c = get_random_other()
                res.append(c)
            else:
                res.append(item)

    return ''.join(res)

# ************************************************************************* #

def generate_node(node: Node, limit: int = 1000) -> str:
    """
    Generate node string.
    """

    res = []
    stack = [node]

    while len(stack) > 0 and len(stack) < limit:
        item = stack.pop()

        print(item)

        if isinstance(item, Node):

            if len(item.tokens) == 0:
                raise RuntimeError("Incomplete node '{}' specification".format(item.name))

            # Choose one rule
            items = random.choice(item.tokens)

            items = items.copy()
            items.reverse()
            stack = stack + items
        elif isinstance(item, Token):
            res.append(generate_token(item))
        else:
            res.append(item)

    return ' '.join(res)

# ************************************************************************* #
