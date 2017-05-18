# -*- coding: utf-8 -*-

"""
.. module:: pyessv._governance.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulate govenerance features.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyessv._constants import GOVERNANCE_STATUS_ACCEPTED
from pyessv._constants import GOVERNANCE_STATUS_DEPRECATED
from pyessv._constants import GOVERNANCE_STATUS_PENDING
from pyessv._constants import GOVERNANCE_STATUS_REJECTED
from pyessv._model import Authority
from pyessv._model import Scope
from pyessv._model import Collection
from pyessv._model import Term
from pyessv._model import NODE_TYPESET



def accept(target):
    """Marks node as accepted.

    """
    _apply(target, pyessv.GOVERNANCE_STATUS_ACCEPTED)


def deprecate(target):
    """Marks node as deprecated.

    """
    _apply(target, pyessv.GOVERNANCE_STATUS_DEPRECATED)


def destroy(target):
    """Marks node for removal from all persistant state stores.

    """
    _apply(target, pyessv.GOVERNANCE_STATUS_DEPRECATED)


def reject(target):
    """Marks node as rejected.

    """
    _apply(target, pyessv.GOVERNANCE_STATUS_REJECTED)


def reset(target):
    """Resets node status.

    """
    _apply(target, pyessv.GOVERNANCE_STATUS_PENDING)


def _apply(target, status):
	if type(target) not in NODE_TYPESET:
		raise TypeError("Cannot apply governance status to a non domain node")

	# Update status.
	target.status = status

	# Cascade.
	children = []
	if isinstance(target, Authority):
		children = target.scopes
	elif isinstance(target, Scope):
		children = target.collections
	elif isinstance(target, Collection):
		children = target.terms
	for child in children:
		_apply(child, status)