import os
import sqlite3
import unicodedata
import fontunicode.glyphlist


abbreviations = {
    '<=': '\N{LESS-THAN OR EQUAL TO}',
    '>=': '\N{GREATER-THAN OR EQUAL TO}',
    'eps': '\N{GREEK SMALL LETTER EPSILON}',
    'sqrt': '\N{SQUARE ROOT}',
}


def search(needle):
    results = [k for k in (abbreviations or {}).keys() if k.startswith(needle)]
    db_filepath = os.path.join(os.path.dirname(fontunicode.glyphlist.__file__), 'unicode.db')
    con = sqlite3.connect(db_filepath, isolation_level=None)
    cur = con.cursor()
    cur.execute(
    """SELECT unilongname
    FROM Unicodes WHERE unilongname LIKE ?""", (needle + '%',))
    results.extend(result[0] for result in cur.fetchall())
    return results


def lookup(needle):
    try:
        return abbreviations[needle]
    except KeyError:
        return unicodedata.lookup(needle)


def try_lookup(needle):
    try:
        return lookup(needle)
    except KeyError:
        return ''


def get_greek_abbreviations():
    prefix = 'GREEK CAPITAL LETTER '
    for l in search(prefix):
        try:
            g, c, l, name = l.split()
        except ValueError:
            continue
        try:
            upper = unicodedata.lookup('GREEK CAPITAL LETTER %s' % name)
            lower = unicodedata.lookup('GREEK SMALL LETTER %s' % name)
        except KeyError:
            continue
        yield name.lower(), lower
        yield name[0].upper() + name[1:].lower(), upper


def get_script_abbreviations():
    for d in range(10):
        _digit, name = unicodedata.name(str(d)).split()
        yield '^%s' % d, unicodedata.lookup('SUPERSCRIPT %s' % name)
        yield '_%s' % d, unicodedata.lookup('SUBSCRIPT %s' % name)
    for c in '()':
        name = unicodedata.name(c)
        yield '^%s' % c, unicodedata.lookup('SUPERSCRIPT %s' % name)
        yield '_%s' % c, unicodedata.lookup('SUBSCRIPT %s' % name)


abbreviations.update(get_greek_abbreviations())
abbreviations['lambda'] = abbreviations['lamda']
abbreviations['Lambda'] = abbreviations['Lamda']
abbreviations.update(get_script_abbreviations())
