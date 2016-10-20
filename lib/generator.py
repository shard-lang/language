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

def generate(rules, start):
    """
    Generate random sequence according to given rules.

    rules: A dictionary of rules.
    start: Starting rule name.
    """

    res = ""
    stack = [format_non_terminal(start)]

    while len(stack) > 0:
        item = stack.pop()

        # Terminal
        if is_non_terminal(item):
            items = copy(random.choice(rules[item]))
            items.reverse()
            stack = stack + items
        else:
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

    print(generate(parse(sys.argv[1]), sys.argv[2]))

# ************************************************************************* #