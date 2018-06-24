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
"""

# ************************************************************************* #

import sys
from lib.parser import parse

# ************************************************************************* #

desc = parseFile('shard-lex.yaml')

macroFormat = False

if len(sys.argv) > 1:
    macroFormat = sys.argv[1] == "macro"

# Print tokens
for token in desc.tokens:
    if macroFormat:
        print("TOKEN({})".format(token.name))
    else:
        print(token.name)

# ************************************************************************* #
