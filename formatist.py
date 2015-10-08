"""
A Python library to convert from older `%` style format strings, to newer
`{}` style.
"""

import re


__all__ = [
    'convert',
]


def convert(fmtstr):
    """Convert %-style format specifiers in `fmtstr` to {}-style specifiers

    >>> convert("Hello %(name)s. It's %(temp).1f C")
    "Hello {name!s:}. It's {temp:>.1f} C"
    """
    oldFormatString = fmtstr
    matches = re.finditer(r"(%)(\((?P<name>.*?)\))"
                          r"(?P<flags>[ #0\-\+])?"
                          r"(?P<minimum>(\*|\d*))"
                          r"(?P<precision>\.(\*|\d*))?"
                          r"(?P<conversion>[diouxXeEfFgGcrs%])",
                          oldFormatString)
    result = []
    previousEnd = 0
    for match in matches:
        result.append(oldFormatString[previousEnd:match.start()])
        conv = match.group("conversion")
        if conv in 'sr':
            bang = "!" + conv
            colon = ":"
        else:
            bang = ""
            fill = match.group("flags") or ""
            align = ">"
            sign = ""
            sharp = ""
            zero = ""
            width = match.group("minimum") or ""
            comma = ""
            precision = match.group("precision") or ""
            ctype = conv
            colon = ":" + (fill + align + sign + sharp + zero + width + comma +
                           precision + ctype)
        result.append("{" + match.group("name") + bang + colon + "}")
        previousEnd = match.end()
    result.append(oldFormatString[previousEnd:])
    return ''.join(result)

