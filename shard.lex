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

EOL:
    0x0D
    0x0A
    0x0D 0x0A

WHITE_SPACE:
    SPACE
    SPACE WHITE_SPACE

SPACE:
    0x20
    0x09

COMMENT:
    BLOCK_COMMENT
    LINE_COMMENT

BLOCK_COMMENT:
    '/*' CHARACTERS '*/'

LINE_COMMENT:
    '//' CHARACTERS EOL

CHARACTERS:
    CHARACTER
    CHARACTER CHARACTERS

LETTER:
    'a'
    'b'
    'c'
    'd'
    'e'
    'f'
    'g'
    'h'
    'i'
    'j'
    'k'
    'l'
    'm'
    'n'
    'o'
    'p'
    'q'
    'r'
    's'
    't'
    'u'
    'v'
    'w'
    'x'
    'y'
    'z'
    'A'
    'B'
    'C'
    'D'
    'E'
    'F'
    'G'
    'H'
    'I'
    'J'
    'K'
    'L'
    'M'
    'N'
    'O'
    'P'
    'Q'
    'R'
    'S'
    'T'
    'U'
    'V'
    'W'
    'X'
    'Y'
    'Z'

IDENTIFIER:
    IDENTIFIER_START
    IDENTIFIER_START IDENTIFIER_CHARS

IDENTIFIER_CHARS:
    IDENTIFIER_CHAR
    IDENTIFIER_CHAR IDENTIFIER_CHARS

IDENTIFIER_START:
    '_'
    LETTER

IDENTIFIER_CHAR:
    IDENTIFIER_START
    DECIMAL_DIGIT

STRING_LITERAL:
    '"' STRING_LITERAL_CHARACTERS '"'

STRING_LITERAL_CHARACTERS:
    STRING_LITERAL_CHARACTER
    STRING_LITERAL_CHARACTER STRING_LITERAL_CHARACTERS

STRING_LITERAL_CHARACTER:
    CHARACTER
    ESCAPE_SEQUENCE
    EOL

ESCAPE_SEQUENCE:
    '\''
    '\"'
    '\?'
    '\\'
    '\0'
    '\a'
    '\b'
    '\f'
    '\n'
    '\r'
    '\t'
    '\v'

CHAR_LITERAL:
    ''' CHAR_LITERAL_CHARACTER '''

CHAR_LITERAL_CHARACTER:
    CHARACTER
    ESCAPE_SEQUENCE

INT_LITERAL:
    DECIMAL_INTEGER
    BINARY_INTEGER
    HEXADECIMAL_INTEGER

DECIMAL_INTEGER:
    '0'
    NON_ZERO_DIGIT
    NON_ZERO_DIGIT DECIMAL_DIGITS

DECIMAL_DIGITS:
    DECIMAL_DIGIT
    DECIMAL_DIGIT DECIMAL_DIGITS

DECIMAL_DIGIT:
    '0'
    NON_ZERO_DIGIT

NON_ZERO_DIGIT:
    '1'
    '2'
    '3'
    '4'
    '5'
    '6'
    '7'
    '8'
    '9'

BINARY_INTEGER:
    BINARY_PREFIX BINARY_DIGITS

BINARY_PREFIX:
    '0b'
    '0B'

BINARY_DIGITS:
    BINARY_DIGIT
    BINARY_DIGIT BINARY_DIGITS

BINARY_DIGIT:
    '0'
    '1'

HEXADECIMAL_INTEGER:
    HEXADECIMAL_PREFIX HEXADECIMAL_DIGITS

HEXADECIMAL_PREFIX:
    '0x'
    '0X'

HEXADECIMAL_DIGITS:
    HEXADECIMAL_DIGIT
    HEXADECIMAL_DIGIT HEXADECIMAL_DIGITS

HEXADECIMAL_DIGIT:
    DECIMAL_DIGIT
    HEXADECIMAL_LETTER

HEXADECIMAL_LETTER:
    'a'
    'b'
    'c'
    'd'
    'e'
    'f'
    'A'
    'B'
    'C'
    'D'
    'E'
    'F'

FLOAT_LITERAL:
    DECIMAL_INTEGER '.'
    DECIMAL_INTEGER '.' DECIMAL_DIGITS
    DECIMAL_INTEGER '.' DECIMAL_DIGITS DECIMAL_EXPONENT
    '.' DECIMAL_DIGITS
    '.' DECIMAL_DIGITS DECIMAL_EXPONENT
    DECIMAL_INTEGER DECIMAL_EXPONENT

DECIMAL_EXPONENT:
    DECIMAL_EXPONENT_START DECIMAL_DIGITS

DECIMAL_EXPONENT_START:
    'e'
    'E'
    'e+'
    'E+'
    'e-'
    'E-'

SQUARE_LEFT:
    '['

SQUARE_RIGHT:
    ']'

PAREN_LEFT:
    '('

PAREN_RIGHT:
    ')'

BRACE_LEFT:
    '{'

BRACE_RIGHT:
    '}'

PERIOD:
    '.'

AMP:
    '&'

AMP_AMP:
    '&&'

STAR:
    '*'

STAR_EQUAL:
    '*='

PLUS:
    '+'

PLUS_PLUS:
    '++'

PLUS_EQUAL:
    '+='

MINUS:
    '-'

MINUS_MINUS:
    '--'

MINUS_EQUAL:
    '-='

EXCLAIM:
    '!'

EXCLAIM_EQUAL:
    '!='

SLASH:
    '/'

SLASH_EQUAL:
    '/='

PERCENT:
    '%'

PERCENT_EQUAL:
    '%='

LESS:
    '<'

LESS_EQUAL:
    '<='

GREATER:
    '>'

GREATER_EQUAL:
    '>='

CARET:
    '^'

PIPE_PIPE:
    '||'

PIPE_EQUAL:
    '|='

QUESTION:
    '?'

COLON:
    ':'

SEMICOLON:
    ';'

EQUAL:
    '='

EQUAL_EQUAL:
    '=='

COMMA:
    ','

PUNCTUATOR:
    SQUARE_LEFT
    SQUARE_RIGHT
    PAREN_LEFT
    PAREN_RIGHT
    BRACE_LEFT
    BRACE_RIGHT
    PERIOD
    AMP
    AMP_AMP
    STAR
    STAR_EQUAL
    PLUS
    PLUS_PLUS
    PLUS_EQUAL
    MINUS
    MINUS_MINUS
    MINUS_EQUAL
    EXCLAIM
    EXCLAIM_EQUAL
    SLASH
    SLASH_EQUAL
    PERCENT
    PERCENT_EQUAL
    LESS
    LESS_EQUAL
    GREATER
    GREATER_EQUAL
    CARET
    PIPE_PIPE
    PIPE_EQUAL
    QUESTION
    COLON
    SEMICOLON
    EQUAL
    EQUAL_EQUAL
    COMMA

KEYWORD:
    'class'
    'public'
    'protected'
    'private'
    'var'
    'auto'
    'int'
    'char'
    'bool'
    'float'
    'string'
    'null'
    'true'
    'false'
    'if'
    'else'
    'do'
    'while'
    'for'

TOKEN:
    IDENTIFIER
    STRING_LITERAL
    CHAR_LITERAL
    INT_LITERAL
    FLOAT_LITERAL
    KEYWORD
    PUNCTUATOR

TOKENS:
    TOKEN
    TOKEN WHITE_SPACE TOKENS

# ************************************************************************* #