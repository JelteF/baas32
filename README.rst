baas32
================

A Python module implementing the alternate base32 encoding as described
by Douglas Crockford at: http://www.crockford.com/wrmg/base32.html.

In `baas32`, this encoding is slightly altered.

He designed the encoding to:

   * Be human and machine readable
   * Be compact
   * Be error resistant
   * Be pronounceable

It uses a symbol set of 10 digits and 22 letters, excluding I, L O and
S. Decoding is not case sensitive, and 'i' and 'l' are converted to '1', 'o' is
converted to '0' and 's' is converted to '5'. Encoding uses only upper-case
characters.

Hyphens may be present in symbol strings to improve readability, and
are removed when decoding.

A check symbol can be appended to a symbol string to detect errors
within the string.

Installation
------------

To install, simply run::

   pip install git+git@github.com:viaict/baas32.git

Usage
-----

Basic usage example::

   >>> import baas32
   >>> baas32.encode(42)
   '1A'
   >>> baas32.decode('1A')
   42
   >>> baas32.encode(42, checksum=True)
   '1A5'
   >>> baas32.decode('1A5', checksum=True)
   42
   >>> baas32.normalize('La5')
   '1A5'

Encode
~~~~~~

::

   baas32.encode(n[, checksum=False[, split=0]])

Encode an integer into a symbol string.

When ``True``, optional ``checksum`` causes a check symbol to be
calculated and appended to the string. This can help detect errors
when decoding.

When specified, optional ``split`` causes the output string to be
divided into clusters of that size separated by hyphens.

Decode
~~~~~~

::

   baas32.decode(s[, checksum=False[, strict=False]])

Decode an encoded symbol string.

Optional ``checksum`` can be provided as a counterpart to the same
argument when encoding. When ``True``, the trailing check symbol is
stripped off and validated. If the check symbol validation fails, a
``ValueError`` is raised.

When ``True``, optional ``strict`` causes a ``ValueError`` to be
raised if the symbol string requires normalization.

Normalize
~~~~~~~~~

::

   baas32.normalize(s[, strict=False])

Normalize an encoded symbol string by applying these transformations:

   #. Remove hyphens
   #. Replace 'I' and 'L' with '1'
   #. Replace 'O' with '0'
   #. Replace 'S' with '5'
   #. Convert all characters to uppercase

Ordinarily this function is automatically used when decoding, but
can be utilized independently to clean or validate a symbol string.
Invalid characters within the normalized string causes a
``ValueError`` to be raised.

When ``True``, optional ``strict`` causes a ``ValueError`` to be
raised if the symbol string requires normalization.

Changelog
---------

Version 0.3.1

   * Forked and fully renamed
   * Allow `u`
   * Change `s` to `5`

Version 0.3.0

   * Add Python 2.6 support
   * Add Python 3.3 and 3.4 support

Version 0.2.0

   * Add optional split parameter when encoding

Version 0.1.0

   * Initial release
