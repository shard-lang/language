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
from parser import is_non_terminal, format_non_terminal

# ************************************************************************* #

def get_random_unicode():
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

def generate(rules, start):
    """
    Generate random sequence according to given rules.

    rules: A dictionary of rules.
    start: Starting rule name.
    """

    res = ""
    sQuote = False
    dQuote = False
    stack = [format_non_terminal(start)]

    while len(stack) > 0:
        item = stack.pop()

        # Terminal
        if is_non_terminal(item):
            # Special placeholder
            if item == format_non_terminal("UTF8_CHAR"):
                c = get_random_unicode()

                # Escape quote charaters
                if c == '"' and dQuote:
                    c = '\\"'
                elif c == "'" and sQuote:
                    c = "\\'"
                elif c == "\\":
                    c = "\\\\";

                res = res + c
            else:
                items = copy(random.choice(rules[item]))
                items.reverse()
                stack = stack + items
        else:
            if item == "'":
                sQuote = not sQuote;
            elif item =='"':
                dQuote = not dQuote;

            res = res + item

    return res

# ************************************************************************* #

if __name__ == "__main__":
    import sys
    import pprint
    from parser import parse

    if len(sys.argv) < 3:
        print("Missing arguments: <filename> <start>")
        exit(-1)

    str = generate(parse(sys.argv[1]), sys.argv[2])

    #print(":".join("{:02x}".format(ord(c)) for c in str))
    print(str)

# ************************************************************************* #