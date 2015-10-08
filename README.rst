bracesformat
============

A Python library to convert from older `%` style format strings, to newer
`{}` style.

.. code:: python

    >>> from format_translator import translateFormatString
    >>> greeting = "Hello %(name)s. It's %(temp).1f C"
    >>> print(greeting % {'name': 'Alice', 'temp': 23.45678})
    Hello Alice. It's 23.5 C
    >>> greeting2 = translateFormatString(greeting)
    >>> print(greeting2)
    Hello {name!s:}. It's {temp:>.1f} C
    >>> print(greeting2.format(name='Alice', temp=23.45678))
    Hello Alice. It's 23.5 C
