#!/usr/bin/env python3

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

"""
Script which extracts a list of tokens and punctuators from lexical description.

Optional 'macro' argument can be passed which generates lines in format:
  `TOKEN(name)`
  `PUNCTUATOR(name, "punc")`
"""

import sys
import re
from lib.parser import format_non_terminal, parse

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')

def to_non_terminal(name):
    """
    see: http://stackoverflow.com/a/1176023
    """
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).upper()

macroFormat = False

if len(sys.argv) > 1:
    macroFormat = sys.argv[1] == "macro"

tokens = []
punctuators = []

with open("shard.lex", 'r') as file:
    for line in file.readlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("# TOKEN: "):
            tokens.append(line[len("# TOKEN: "):])

        if line.startswith("# PUNCTUATOR: "):
            punctuators.append(line[len("# PUNCTUATOR: "):])

# Print tokens
for token in tokens:
    if macroFormat:
        print("TOKEN({})".format(token))
    else:
        print(token)

# Required for punctuator strings
rules = parse("shard.lex")

# Print punctuators
for punctuator in punctuators:
    if macroFormat:
        str = rules[format_non_terminal(to_non_terminal(punctuator))][0][0]
        print("PUNCTUATOR({}, \"{}\")".format(punctuator, str))
    else:
        print(punctuator)
