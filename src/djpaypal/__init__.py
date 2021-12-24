import pkg_resources
from . import checks  # noqa: Register the checks


__version__ = pkg_resources.require("djpaypal")[0].version
