from unittest import TestCase

import formatist


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
                              formatist.convert(format).format(**fields))
        check("before %(hello)s after", hello='asdf')
        check("%(hello)r between %(number)d", hello='jkl;', number=7)
        check("%(hexify)x", hexify=4321)
        check("%(floatnum)f", floatnum=3.4567)
        check("%(floatnum)0.6f", floatnum=3.4567)
        check("%(floatnum)08.2f", floatnum=3.4567)
        check("%(floatnum) 8.2f", floatnum=3.4567)

