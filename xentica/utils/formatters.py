"""The collection of formatters."""


def sizeof_fmt(num, suffix=''):
    """
    Format the number with the humanized order of magnitude.

    In example, ``11234`` become ``11.23K``.

    :param num:
        The positive integer.
    :param suffix:
        Additional suffix to add to formatted string.

    :returns:
        Formatted number as a string.

    """
    if abs(num) < 1000:
        return "%s%s" % (num, suffix)
    for unit in ['K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        num /= 1000.0
        if abs(num) < 1000.0:
            return "%.2f%s%s" % (num, unit, suffix)
    num /= 1000.0
    return "%.2f%s%s" % (num, 'Y', suffix)
