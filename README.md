# yet_another_ini

Yet another .ini clone. Has one feature that .ini lacks.

File extension should be .yai, idk. This thing will never be popular

# Installation

Yes, this shit is also available on pypi.

`pip install yet_another_ini`

# Format

```
key=value
key=value
just a key (its value will be None)

[ header ]
key=value
key=value
just a key (its value will be None)

< special header >
list element 1
list element 2
list element 3
(this is a list of strings)
```

Whitespaces and empty lines are optional

# API

Just look at the source code (especially `__init__.py`) or use autocompletion,
I don't want to write the proper doc cuz I made it for myself
