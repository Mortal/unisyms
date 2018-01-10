Unisyms
=======

Python 3 script for Unicode character searching in Vim.

Usage
-----

Press `CTRL-B` in insert mode to insert a Unicode character by name,
e.g. `GREEK SMALL LETTER GAMMA`. There are also some shorthands defined
in unisyms.py for `<=`, `>=`, `eps`, `sqrt`, Greek upper/lowercase letters,
super/subscript digits e.g. `^2`, `_5`, and parentheses `^(`, `_)`.
Completion is supported.

Invoke `:Uniname` on a range of lines to replace non-ASCII characters
with their named-escape equivalent in Python, e.g. `γ` is replaced by
`\N{GREEK SMALL LETTER GAMMA}`.

Installation
------------

Requires fontunicode: `pip install --user git+https://github.com/Mortal/font-unicode`.

Copy/symlink unisyms.py into `~/.vim/python3` and add `source path/to/unisyms.vim` in your `.vimrc`.
