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
Generate DOT output from description file.
"""

# ************************************************************************* #

import sys
from lib.parser import parseFile, Rule

# ************************************************************************* #

if len(sys.argv) < 2:
    print("Missing arguments: <filename>")
    exit(-1)

desc = parseFile(sys.argv[1])

lines = []

for token in desc.tokens:
    lines.append("  Token -> " + token.name)

    if token.name != token.rule.name:
        lines.append("  " + token.name + " -> " + token.rule.name)

# Rules
for rule in desc.rules:
    lines.append("  " + rule.name)
    for item in rule.rules:
        for item2 in item:
            if isinstance(item2, Rule):
                lines.append("  " + rule.name + " -> " + item2.name)
            #else:
            #    lines.append("  " + rule.name + " -> \"" + item2 + "\"")

print("digraph {");

for line in set(lines):
    print(line + ";")

print("}");

# ************************************************************************* #
