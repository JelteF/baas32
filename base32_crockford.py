"""
base32-crockford
================

A Python module implementing the alternate base32 encoding as described
by Douglas Crockford at: http://www.crockford.com/wrmg/base32.html.

According to his description, the encoding is designed to:

   * Be human and machine readable
   * Be compact
   * Be error resistant
   * Be pronounceable

It uses a symbol set of 10 digits and 22 letters, excluding I, L O and
U. When decoding, the letters 'i' and 'l' are converted to '1' and 'o'
is converted to '0'. Decoding is not case sensitive and encoding uses
only upper-case characters.

Hyphens may be present anywhere in a symbol string to improve
readability and are ignored when decoding.

A check symbol may be appended to a symbol string for error detection
when decoding the string.

"""

import re
import string


__all__ = ["encode", "decode", "normalize"]


bytes_types = (bytes, bytearray)
string_types = (str, unicode)

# The encoded symbol space does not include I, L, O or U
symbols = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
# These five symbols are exclusively for checksum values
check_symbols = '*~$=U'

encode_symbols = {i: ch for (i, ch) in enumerate(symbols + check_symbols)}
decode_symbols = {ch: i for (i, ch) in enumerate(symbols + check_symbols)}
normalize_symbols = string.maketrans('IiLlOo', '111100')
valid_symbols = re.compile('^[%s]+[%s]?$' % (symbols,
                                             re.escape(check_symbols)))

base = len(symbols)
check_base = len(symbols + check_symbols)


def encode(number, checksum=False):
    """Encode an integer into a symbol string.

    A ValueError is raised on invalid input.

    If checksum is set to True, a check symbol will be
    calculated and appended to the string.

    The encoded string is returned.
    """
    number = int(number)
    if number < 0:
        raise ValueError("number '%d' is not a positive integer" % number)

    check_symbol = ''
    if checksum:
        check_symbol = encode_symbols[number % check_base]

    if number == 0:
        return '0' + check_symbol

    symbol_string = ''
    while number > 0:
        remainder = number % base
        number //= base
        symbol_string = encode_symbols[remainder] + symbol_string

    return symbol_string + check_symbol


def decode(symbol_string, checksum=False, strict=False):
    """Decode an encoded symbol string.

    If checksum is set to True, the string is assumed to have a
    trailing check symbol which will be validated. If the
    checksum validation fails, a ValueError is raised.

    If strict is set to True, a ValueError is raised if the
    normalization step requires changes to the string.

    The decoded string is returned.
    """
    symbol_string = normalize(symbol_string, strict=strict)
    if checksum:
        symbol_string, check_symbol = symbol_string[:-1], symbol_string[-1]

    number = 0
    for symbol in symbol_string:
        number = number * base + decode_symbols[symbol]

    if checksum:
        check_value = decode_symbols[check_symbol]
        modulo = number % check_base
        if check_value != modulo:
            raise ValueError("invalid check symbol '%s' for string '%s'" %
                             (check_symbol, symbol_string))

    return number


def normalize(symbol_string, strict=False):
    """Normalize an encoded symbol string.

    Normalization provides error correction and prepares the
    string for decoding. These transformations are applied:

       0. Encoded as ASCII, if necessary
       1. Hyphens are removed
       2. 'I', 'i', 'L' or 'l' are converted to '1'
       3. 'O' or 'o' are converted to '0'
       4. All characters are converted to uppercase

    A TypeError is raised if an invalid string type is provided.

    A ValueError is raised if the normalized string contains
    invalid characters.

    If the strict parameter is set to True, a ValueError is raised
    if any of the above transformations are applied.

    The normalized string is returned.
    """
    if isinstance(symbol_string, bytes_types):
        pass
    elif isinstance(symbol_string, string_types):
        try:
            symbol_string = symbol_string.encode('ascii')
        except UnicodeEncodeError:
            raise ValueError("string should only contain ASCII characters")
    else:
        raise TypeError("string should be bytes or ASCII, not %s" %
                        symbol_string.__class__.__name__)
    string = symbol_string.translate(normalize_symbols, '-').upper()

    if not valid_symbols.match(string):
        raise ValueError("string '%s' contains invalid characters" % string)

    if strict and string != symbol_string:
        raise ValueError("string '%s' requires normalization" % symbol_string)

    return string
