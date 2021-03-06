# -*- coding: utf-8 -*-

"""
.. module:: map_c3s_cordex.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Maps C3S-CORDEX ESGF publisher ini file to normalized pyessv format.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
from utils import yield_comma_delimited_options
from utils import yield_pipe_delimited_options


# TODO process map: rcm_name_map = map(project, rcm_model : rcm_name)

# Vocabulary collections extracted from ini file.
COLLECTIONS = {
	('domain', lambda: yield_domain),
	('driving_model', yield_comma_delimited_options),
	('ensemble', r'r[0-9]+i[0-9]+p[0-9]+'),
	('experiment', yield_pipe_delimited_options),
	('institute', yield_comma_delimited_options),
	('product', yield_comma_delimited_options),
	('rcm_model', yield_comma_delimited_options),
	('rcm_name', lambda: yield_rcm_name),
	('rcm_version', yield_comma_delimited_options),
	('thredds_exclude_variables', yield_comma_delimited_options),
	('time_frequency', yield_comma_delimited_options),
	('variable', yield_comma_delimited_options),
	('version', r'v^[0-9]*$')
}

# Fields extracted from ini file & appended as data to the scope.
SCOPE_DATA = {
	'filename_format',
	'directory_format',
	'dataset_id'
}


def yield_domain(ctx):
	"""Yields domain information to be converted to pyessv terms.

	"""
	for domain_name, domain_description in ctx.ini_section.get_option('domain_description_map', '\n', '|'):
		yield domain_name, domain_name, domain_description


def yield_rcm_name(ctx):
	"""Yields rcm name information to be converted to pyessv terms.

	"""
	for _, rcm_name in ctx.ini_section.get_option('rcm_name_map', '\n', '|'):
		yield rcm_name
