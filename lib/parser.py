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

import yaml
from typing import Optional, List, Union

# ************************************************************************* #

class Rule:
    def __init__(self, name: str, rules: List[List[Union['Rule', str]]]):
        self.name = name
        self.rules = rules

    def __repr__(self) -> str:
        return "{} ({}, {})".format(self.__class__.__name__, self.name, len(self.rules))

    def __str__(self) -> str:
        return "{} ({})".format(self.name, len(self.rules))

# ************************************************************************* #

class Token:
    def __init__(self, name: str, rule: Rule):
        self.name = name
        self.rule = rule

    def __repr__(self) -> str:
        return "{} ({}, {})".format(self.__class__.__name__, self.name, self.rule.name)

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.rule.name)

# ************************************************************************* #

class Node:
    def __init__(self, name: str, tokens: List[List[Union['Node', Token, str]]]):
        self.name = name
        self.tokens = tokens

    def __repr__(self) -> str:
        return "{} ({}, {})".format(self.__class__.__name__, self.name, len(self.tokens))

    def __str__(self) -> str:
        return "{} ({})".format(self.name, len(self.tokens))

# ************************************************************************* #

class Description:
    def __init__(self):
        self.rules = []
        self.tokens = []
        self.nodes = []

    def __add__(self, source: 'Description') -> 'Description':
        self.rules = self.rules + source.rules
        self.tokens = self.tokens + source.tokens
        self.nodes = self.nodes + source.nodes
        return self

    def rule(self, name: str) -> Optional[Rule]:
        for rule in self.rules:
            if rule.name == name:
                return rule

        return None

    def token(self, name: str) -> Optional[Token]:
        for token in self.tokens:
            if token.name == name:
                return token

        return None

    def node(self, name: str) -> Optional[Node]:
        for node in self.nodes:
            if node.name == name:
                return node

        return None

# ************************************************************************* #

def _add_item(desc: Description, lst: list, item):
    """
    Add value to list.
    """

    if isinstance(item, list):
        for i in item:
            _add_item(desc, lst, i)
    elif isinstance(item, str):
        lst.append(item)
    elif isinstance(item, int):
        # Convert ordinal value to string
        lst.append(chr(item))

# ************************************************************************* #

def parse(source: str) -> Description:
    """
    Parse description string.

    source: The source string.
    return: Description file structure.
    """

    data = yaml.load(source)

    desc = Description()

    # Import other files
    if 'includes' in data:
        for include in data['includes']:
            desc = desc + parseFile(include)

    if 'rules' in data:
        rules = data['rules']

        for name in rules:
            rule = desc.rule(name)

            if rule is None:
                rule = Rule(name, [])

            desc.rules.append(rule)

            # Can be empty list
            if rules[name] is not None:
                for line in rules[name]:
                    lst = []
                    _add_item(desc, lst, line)
                    rule.rules.append(lst)

        # Foreach all rules and add references between them
        for rule in desc.rules:
            for ruleItem in rule.rules:
                for i in range(len(ruleItem)):
                    item = desc.rule(ruleItem[i])
                    if item is not None:
                        ruleItem[i] = item

    if 'tokens' in data:
        tokens = data['tokens']

        for name in tokens:
            desc.tokens.append(Token(name, desc.rule(tokens[name])))

    if 'nodes' in data:
        nodes = data['nodes']

        for name in nodes:
            node = desc.node(name)

            if node is None:
                node = Node(name, [])

            desc.nodes.append(node)

            # Can be empty list
            if nodes[name] is not None:
                for line in nodes[name]:
                    lst = []
                    _add_item(desc, lst, line)
                    node.tokens.append(lst)

        # Foreach all nodes and add references between them
        for node in desc.nodes:
            for nodeItem in node.tokens:
                for i in range(len(nodeItem)):
                    item1 = desc.token(nodeItem[i])
                    item2 = desc.node(nodeItem[i])
                    if item1 is not None:
                        nodeItem[i] = item1
                    elif item2 is not None:
                        nodeItem[i] = item2

    return desc

# ************************************************************************* #

def parseFile(filename):
    """
    Parse description file.

    filename: Path to source file.
    return: Description file structure.
    """
    with open(filename) as f:
        return parse(f.read())

# ************************************************************************* #
