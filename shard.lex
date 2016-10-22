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

# TOKEN: Comment
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

CHARACTER:
    UTF8_CHAR

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

# TOKEN: Identifier
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

# TOKEN: StringLiteral
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

# TOKEN: CharLiteral
CHAR_LITERAL:
    ''' CHAR_LITERAL_CHARACTER '''

CHAR_LITERAL_CHARACTER:
    CHARACTER
    ESCAPE_SEQUENCE

# TOKEN: IntLiteral
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

# TOKEN: FloatLiteral
FLOAT_LITERAL:
    DECIMAL_INTEGER '.' DECIMAL_DIGITS
    DECIMAL_INTEGER '.' DECIMAL_DIGITS DECIMAL_EXPONENT
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

# PUNCTUATOR: SquareLeft
SQUARE_LEFT:
    '['

# PUNCTUATOR: SquareRight
SQUARE_RIGHT:
    ']'

# PUNCTUATOR: ParenLeft
PAREN_LEFT:
    '('

# PUNCTUATOR: ParenRight
PAREN_RIGHT:
    ')'

# PUNCTUATOR: BraceLeft
BRACE_LEFT:
    '{'

# PUNCTUATOR: BraceRight
BRACE_RIGHT:
    '}'

# PUNCTUATOR: Period
PERIOD:
    '.'

# PUNCTUATOR: Amp
AMP:
    '&'

# PUNCTUATOR: AmpEqual
AMP_EQUAL:
    '&='

# PUNCTUATOR: AmpAmp
AMP_AMP:
    '&&'

# PUNCTUATOR: AmpAmpEqual
AMP_AMP_EQUAL:
    '&&='

# PUNCTUATOR: Star
STAR:
    '*'

# PUNCTUATOR: StarEqual
STAR_EQUAL:
    '*='

# PUNCTUATOR: Plus
PLUS:
    '+'

# PUNCTUATOR: PlusPlus
PLUS_PLUS:
    '++'

# PUNCTUATOR: PlusEqual
PLUS_EQUAL:
    '+='

# PUNCTUATOR: MinusEqual
MINUS:
    '-'

# PUNCTUATOR: MinusMinus
MINUS_MINUS:
    '--'

# PUNCTUATOR: MinusEqual
MINUS_EQUAL:
    '-='

# PUNCTUATOR: Tilde
TILDE:
    '~'

# PUNCTUATOR: Exclaim
EXCLAIM:
    '!'

# PUNCTUATOR: ExclaimEqual
EXCLAIM_EQUAL:
    '!='

# PUNCTUATOR: Slash
SLASH:
    '/'

# PUNCTUATOR: SlashEqual
SLASH_EQUAL:
    '/='

# PUNCTUATOR: Percent
PERCENT:
    '%'

# PUNCTUATOR: PercentEqual
PERCENT_EQUAL:
    '%='

# PUNCTUATOR: Less
LESS:
    '<'

# PUNCTUATOR: LessLess
LESS_LESS:
    '<<'

# PUNCTUATOR: LessEqual
LESS_EQUAL:
    '<='

# PUNCTUATOR: LessLessEqual
LESS_LESS_EQUAL:
    '<<='

# PUNCTUATOR: Greater
GREATER:
    '>'

# PUNCTUATOR: GreaterGreater
GREATER_GREATER:
    '>>'

# PUNCTUATOR: GreaterEqual
GREATER_EQUAL:
    '>='

# PUNCTUATOR: GreaterGreaterEqual
GREATER_GREATER_EQUAL:
    '>>='

# PUNCTUATOR: Caret
CARET:
    '^'

# PUNCTUATOR: CaretEqual
CARET_EQUAL:
    '^='

# PUNCTUATOR: Pipe
PIPE:
    '|'

# PUNCTUATOR: PipePipe
PIPE_PIPE:
    '||'

# PUNCTUATOR: PipeEqual
PIPE_EQUAL:
    '|='

# PUNCTUATOR: PipePipeEqual
PIPE_PIPE_EQUAL:
    '||='

# PUNCTUATOR: Question
QUESTION:
    '?'

# PUNCTUATOR: Colon
COLON:
    ':'

# PUNCTUATOR: Semicolon
SEMICOLON:
    ';'

# PUNCTUATOR: Equal
EQUAL:
    '='

# PUNCTUATOR: EqualEqual
EQUAL_EQUAL:
    '=='

# PUNCTUATOR: Comma
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
    AMP_EQUAL
    AMP_AMP
    AMP_AMP_EQUAL
    STAR
    STAR_EQUAL
    PLUS
    PLUS_PLUS
    PLUS_EQUAL
    MINUS
    MINUS_MINUS
    MINUS_EQUAL
    TILDE
    EXCLAIM
    EXCLAIM_EQUAL
    SLASH
    SLASH_EQUAL
    PERCENT
    PERCENT_EQUAL
    LESS
    LESS_LESS
    LESS_EQUAL
    LESS_LESS_EQUAL
    GREATER
    GREATER_GREATER
    GREATER_EQUAL
    GREATER_GREATER_EQUAL
    CARET
    CARET_EQUAL
    PIPE
    PIPE_PIPE
    PIPE_EQUAL
    PIPE_PIPE_EQUAL
    QUESTION
    COLON
    SEMICOLON
    EQUAL
    EQUAL_EQUAL
    COMMA

# TOKEN: Keyword
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
    'try'
    'catch'
    'throw'

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