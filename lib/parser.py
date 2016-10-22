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

import re
import string

# ************************************************************************* #

def _format_items(items):
    """
    Reformat items from rule.

    items: Items to reformat.
    return: Reformatted items.
    """
    result = []

    for item in items:
        m = re.search("^'(.*)'$", item)
        if m:
            result.append(m.group(1))
        elif item.startswith('0x'):
            result.append(chr(int(item, 0)))
        else:
            result.append(format_non_terminal(item))

    return result

# ************************************************************************* #

def format_non_terminal(name):
    """
    Format non-terminal name.

    name: Non-terminal name.
    return: Result internal representation of non-terminal.
    """
    return "@" + name

# ************************************************************************* #

def is_non_terminal(name):
    """
    Check if name is a non-terminal.

    name: Terminal or non-terminal name.
    return: Is non-terminal?
    """
    return name.startswith("@")

# ************************************************************************* #

def parse(filename):
    """
    Parse description file.

    filename: Path to source file.
    return: Description file structure.
    """
    rules = {}
    ruleName = None
    ruleItems = None

    # Foreach lines
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()

            # Skip comments or empty lines
            if not line or line.startswith("#"):
                continue

            if line.startswith("!include"):
                filename2 = re.split(" ", line)[1]
                rules.update(parse(filename2))
                continue

            # Rule
            if line.endswith(":"):
                if ruleName is not None:
                    rules[format_non_terminal(ruleName)] = ruleItems
                    ruleName = None

                ruleName = line[:-1]
                ruleItems = []
            else:
                ruleItems.append(_format_items(re.split(" ", line)))

        if ruleName is not None:
            rules[format_non_terminal(ruleName)] = ruleItems

        return rules

# ************************************************************************* #

if __name__ == "__main__":
    import sys
    import pprint

    if len(sys.argv) < 2:
        print("Missing arguments: <filename>")
        exit(-1)

    pprint.pprint(parse(sys.argv[1]))

# ************************************************************************* #