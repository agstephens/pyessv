from pyessv.accessors import esdoc_cmip6
from pyessv.accessors import wcrp_cmip6



# Expose accessors mapped by authority.
ACCESSORS = {
	'esdoc': {
		'cmip6': esdoc_cmip6
	},
	'wcrp': {
		'cmip6': wcrp_cmip6
	}
}
