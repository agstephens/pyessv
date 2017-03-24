# -*- coding: utf-8 -*-

"""
.. module:: pyessv.archive.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates access to archive.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyessv._cache import get_cached



def load(authority, scope=None, collection=None, term=None):
    """Loads a CV authority from archive.

    :param str authority: Vocabulary authority, e.g. wcrp.
    :param str scope: Vocabulary scope, e.g. global.
    :param str collection: Vocabulary collection, e.g. institute-id.
    :param str term: Vocabulary term, e.g. ipsl.

    """
    # Format names.
    names = [authority, scope, collection, term]
    names = [_format_name(i) for i in names if i is not None]

    # Set authority (JIT loads cache).
    result = get_cached(names[0])
    if result is None:
        return

    # Return last loaded sub-collection.
    try:
        for name in names[1:]:
            result = result[name]
    except KeyError:
        pass
    else:
        return result


def save():
    """Saves archive to file system.

    """
    pass


def _format_name(name):
    """Formats a name prior to accessing archive.

    """
    if name is not None:
        return unicode(name).strip().lower()