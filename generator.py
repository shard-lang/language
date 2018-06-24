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
from lib.generator import generate_token, generate_node
from lib.parser import parseFile

# ************************************************************************* #

if len(sys.argv) < 2:
    print("Missing arguments: <filename> [ <name> ]")
    exit(-1)

desc = parseFile(sys.argv[1])

if len(sys.argv) < 3:
    print('Available tokens are:\n', '\n '.join([str(t.name) for t in desc.tokens]))
    print('Available nodes are:\n', '\n '.join([str(t.name) for t in desc.nodes]))
    exit(-1)

name = sys.argv[2]
token = desc.token(name)
node = desc.node(name)

if token is not None:
    print(generate_token(token))
elif node is not None:
    print(generate_node(node))
else:
    print(("Token or Node '{}' not found".format(name)))
    print('Available tokens are:\n', '\n '.join([str(t.name) for t in desc.tokens]))
    print('Available nodes are:\n', '\n '.join([str(t.name) for t in desc.nodes]))
    exit(-1)

# ************************************************************************* #
