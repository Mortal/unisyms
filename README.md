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

In the `text` filetype (i.e. in `*.txt` files), backslash in insert mode
is mapped to the same function as `CTRL-B`, except space is mapped to return
while inputting the character name. This allows you to type `\gamma `
(including the space) to insert a γ.

Invoke `:Uniname` on a range of lines to replace non-ASCII characters
with their named-escape equivalent in Python, e.g. `γ` is replaced by
`\N{GREEK SMALL LETTER GAMMA}`.

Installation
------------

Requires fontunicode: `pip install --user git+https://github.com/Mortal/font-unicode`.

Copy/symlink unisyms.py into `~/.vim/python3` and add `source path/to/unisyms.vim` in your `.vimrc`.

TODO
----

Use [mathspec](http://mirrors.dotsrc.org/ctan/macros/xetex/latex/mathspec/mathspec.sty)
and [unicode-math-table](http://mirror.hmc.edu/ctan/macros/latex/contrib/unicode-math/unicode-math-table.tex)
to translate input to `CTRL-B`.
