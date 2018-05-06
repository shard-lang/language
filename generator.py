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
Generate possible source code.
"""

# ************************************************************************* #

import sys
from lib.generator import generate
from lib.parser import parse

# ************************************************************************* #

if len(sys.argv) < 2:
    print("Missing arguments: <filename> <rule>")
    exit(-1)

rule = sys.argv[2]
rules = parse(sys.argv[1])

print(generate(rules, rule))

# ************************************************************************* #
