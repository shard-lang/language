# Shard language description

Repository contains language description files which can be used by some tools. There are also python scripts for
parsing description files and also generator which can be used for generating source files for testing.

## Specification files

There are a few specification files (YAML format) which defines basic language tokens (`shard-lex.yaml`) and AST nodes (`shard-syntax`). The additional specification file `shard-builtin.yaml` defines declarations which are part of the language.

## Tools

### Generator

Program generates random string according to given specification file and required identifier (token or AST node name). If executed without the second argument it prints a list of available values for the second argument.

```bash
./generator.py shard-builtin.yaml DECLARATION
```

## Library

A library for specification files handling.

### Parser

The parser can be used for parsing YAML specification files.

```python
from lib.parser import parse

desc = parseFile('shard-lex.yaml')

# Print tokens
for token in desc.tokens:
    print(token.name)

```

### Generator

A library which is able to generate random code from given specification file.

```python
from lib.generator import generate_token, generate_node
from lib.parser import parseFile

desc = parseFile('shard-builtin.yaml')

# Generate source for AST node
node = desc.node("SOURCE")
print(generate_node(node))

# Generate source for token
token = desc.node("Identifier")
print(generate_token(token))
```
