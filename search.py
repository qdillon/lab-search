"""Search helpers. Complete the five function bodies, then run the doctests."""


def number_lines(lines):
    """
    >>> number_lines(['Library hours', '', 'Open late'])
    [(1, 'Library hours'), (2, ''), (3, 'Open late')]
    >>> number_lines([])
    []
    """
    return list(enumerate(lines, 1))


def matching_lines(lines, query):
    """
    >>> matching_lines(['Library hours', '', 'LIBRARY cafe'], 'library')
    [(1, 'Library hours'), (3, 'LIBRARY cafe')]
    >>> matching_lines(['cat', 'catalog'], '')
    []
    >>> matching_lines(['a.b', 'axb'], '.')
    [(1, 'a.b')]
    >>> matching_lines(['a  b', 'a b'], 'a b')
    [(2, 'a b')]
    >>> matching_lines([], 'x')
    []
    """
    if query == '':
        return []
    q = query.lower()
    return [(num, text) for num, text in number_lines(lines)
            if q in text.lower()]


def group_matches(documents, query):
    """
    >>> documents = [['Library map', 'Open late'], ['Pool hours'], ['Cafe', 'LIBRARY events']]
    >>> group_matches(documents, 'library')
    [[(1, 'Library map')], [], [(2, 'LIBRARY events')]]
    >>> group_matches([[], ['x']], 'x')
    [[], [(1, 'x')]]
    >>> group_matches([], 'x')
    []
    """
    return [matching_lines(doc, query) for doc in documents]


def flatten_matches(names, groups):
    """
    >>> names = ['campus.txt', 'pool.txt', 'events.txt']
    >>> groups = [[(1, 'Library map')], [], [(2, 'LIBRARY events')]]
    >>> flatten_matches(names, groups)
    [('campus.txt', 1, 'Library map'), ('events.txt', 2, 'LIBRARY events')]
    >>> flatten_matches(['a.txt'], [[(1, 'x'), (2, 'x')]])
    [('a.txt', 1, 'x'), ('a.txt', 2, 'x')]
    >>> flatten_matches([], [])
    []
    """
    return [(name, num, text)
            for name, group in zip(names, groups)
            for num, text in group]


def match_counts(names, groups):
    """
    >>> names = ['campus.txt', 'pool.txt', 'events.txt']
    >>> groups = [[(1, 'Library map')], [], [(2, 'LIBRARY events')]]
    >>> match_counts(names, groups)
    {'campus.txt': 1, 'pool.txt': 0, 'events.txt': 1}
    >>> match_counts([], [])
    {}
    """
    return {name: len(group) for name, group in zip(names, groups)}