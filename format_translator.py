import re

from unittest import TestCase


class FormatTranslationTests(TestCase):
    """
    Tests for L{translateFormatString}.
    """

    def test_translateFormatString(self):
        """
        Verify that formatting a given old-style format string(%-based) will
        work.
        """
        def check(format, **fields):
            self.assertEquals(format % fields,
                              translateFormatString(format).format(**fields))
        check("before %(hello)s after", hello='asdf')
        check("%(hello)r between %(number)d", hello='jkl;', number=7)
        check("%(hexify)x", hexify=4321)
        check("%(floatnum)f", floatnum=3.4567)
        check("%(floatnum)0.6f", floatnum=3.4567)
        check("%(floatnum)08.2f", floatnum=3.4567)
        check("%(floatnum) 8.2f", floatnum=3.4567)


def translateFormatString(oldFormatString):
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