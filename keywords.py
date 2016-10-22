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
Script which extracts a list of keywords from lexical description.

Optional 'macro' argument can be passed which generates lines in format:
  `KEYWORD(name, "Name")`
"""

import sys
from lib.parser import format_non_terminal, parse

macroFormat = False

if len(sys.argv) > 1:
    macroFormat = sys.argv[1] == "macro"

rules = parse("shard.lex")
keyword = format_non_terminal("KEYWORD")

if not keyword in rules:
    print("KEYWORD non-terminal not found")
    exit(-1)

keywords = rules[keyword]

for keyword in keywords:
    if macroFormat:
        print("KEYWORD({}, \"{}\")".format(keyword[0].capitalize(), keyword[0]))
    else:
        print(keyword[0])
