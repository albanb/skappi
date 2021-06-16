"""
The entry point for skappi.
"""

import sys

if __package__ == "":
    from skappi import main  # pylint: disable=no-name-in-module
else:
    from skappi.skappi import main


sys.exit(main())
