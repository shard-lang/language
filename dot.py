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

import sys
from lib.parser import parse, is_non_terminal

if len(sys.argv) < 2:
    print("Missing arguments: <filename>")
    exit(-1)

rules = parse(sys.argv[1])
lines = []

# Rules
for rule, items in rules.items():
    lines.append("  " + rule[1:])
    for item in items:
        for item2 in item:
            if is_non_terminal(item2):
                lines.append("  " + rule[1:] + " -> " + item2[1:])

print("digraph {");

for line in set(lines):
    print(line + ";")

print("}");
