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

import unittest
from parser import *

# ************************************************************************* #

class TestParser(unittest.TestCase):

    def test_rule(self):
        rule = Rule("name", [])
        self.assertEqual(rule.name,  "name")
        self.assertEqual(rule.rules, [])

        rule.name = "Test"
        rule.rules = ['a',  'b']
        self.assertEqual(rule.name,  "Test")
        self.assertEqual(rule.rules, ['a',  'b'])

    def test_token(self):
        token = Token("name",  None)
        self.assertEqual(token.name,  "name")
        self.assertEqual(token.rule, None)

        token.name = "Test"
        token.rule = Rule("rule", [])
        self.assertEqual(token.name,  "Test")
        self.assertEqual(token.rule.name, "rule")

    def test_node(self):
        node = Node("name", [])
        self.assertEqual(node.name, "name")
        self.assertEqual(node.tokens, [])

        node.name = "Test"
        node.tokens = ['.', Node("name2", [])]
        self.assertEqual(node.name, "Test")
        self.assertEqual(len(node.tokens), 2)

    def test_parse(self):
        desc = parse("""
rules:
    TOKEN1:
        - t11
        - t12

    TOKEN2:
        - TOKEN1
        - [ t22, t23 ]

tokens:
    Token1: TOKEN1
    Token2: TOKEN2

nodes:
    NODE1:
        - Token1
        - [ Token1, Token2 ]

    NODE2:
        - [ NODE1, '.' ]
""")

        self.assertEqual(len(desc.rules), 2)
        self.assertEqual(len(desc.tokens), 2)
        self.assertEqual(len(desc.nodes), 2)

        rule = desc.rule("TOKEN1")
        self.assertIsNotNone(rule)
        self.assertEqual(rule.name,  "TOKEN1")
        self.assertEqual(len(rule.rules), 2)
        self.assertEqual(len(rule.rules[0]), 1)
        self.assertEqual(rule.rules[0][0], 't11')
        self.assertEqual(len(rule.rules[1]), 1)
        self.assertEqual(rule.rules[1][0], 't12')

        rule = desc.rule("TOKEN2")
        self.assertIsNotNone(rule)
        self.assertEqual(rule.name,  "TOKEN2")
        self.assertEqual(len(rule.rules), 2)
        self.assertEqual(len(rule.rules[0]), 1)
        self.assertEqual(rule.rules[0][0], desc.rule("TOKEN1"))
        self.assertEqual(len(rule.rules[1]), 2)
        self.assertEqual(rule.rules[1][0], 't22')
        self.assertEqual(rule.rules[1][1], 't23')

        # Unknown rule
        self.assertIsNone(desc.rule("TOKEN3"))

        token = desc.token("Token1")
        self.assertIsNotNone(token)
        self.assertEqual(token.name, "Token1")
        self.assertEqual(token.rule, desc.rule("TOKEN1"))

        token = desc.token("Token2")
        self.assertIsNotNone(token)
        self.assertEqual(token.name, "Token2")
        self.assertEqual(token.rule, desc.rule("TOKEN2"))

        # Unknown token
        self.assertIsNone(desc.token("Token3"))

        node = desc.node("NODE1")
        self.assertIsNotNone(node)
        self.assertEqual(node.name, "NODE1")
        self.assertEqual(len(node.tokens), 2)
        self.assertEqual(len(node.tokens[0]), 1)
        self.assertEqual(node.tokens[0][0], desc.token("Token1"))
        self.assertEqual(len(node.tokens[1]), 2)
        self.assertEqual(node.tokens[1][0], desc.token("Token1"))
        self.assertEqual(node.tokens[1][1], desc.token("Token2"))

        node = desc.node("NODE2")
        self.assertIsNotNone(node)
        self.assertEqual(node.name, "NODE2")
        self.assertEqual(len(node.tokens), 1)
        self.assertEqual(len(node.tokens[0]), 2)
        self.assertEqual(node.tokens[0][0], desc.node("NODE1"))
        self.assertEqual(node.tokens[0][1], '.')


# ************************************************************************* #

if __name__ == '__main__':
    unittest.main()

# ************************************************************************* #
