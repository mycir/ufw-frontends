#!/usr/bin/python3

import sys
from ufw_frontends.l10n import ufw_localize

if __name__ == '__main__':
    if sys.argv[1] == 'gtk':
        from ufw_frontends.frontend_gtk import main
    # elif if sys.argv[1] == 'qt':
        # from ufw_frontends.frontend_qt import main
    else:
        sys.exit("Unsupported graphics library.")
    ufw_localize()
    main()
